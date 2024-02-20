#!/usr/bin/env python3

import socket
import time
import requests
import json
import random
from pygame import mixer
from input_card_scanner import CardReader

backend_addr = None

class RaceStation:
    def __init__(self):
        self.read_lane()
        self.setup_udp()
        self.scanner = CardReader()
        self.setup_keyboard()
        self.setup_sound()
        self.running = True
        self.flag = ""
        self.racer_state = ""
        self.pitting = False
        self.play_sounds = False
        self.pos = 0

    def read_lane(self):
        with open('../trackid', 'r') as f:
            self.lane = int(f.readline().strip())
            print(f'Lane {self.lane}')

    def run(self):
        print("Starting")
        while self.running:
            self.process_udp()
            self.process_reader()
            self.process_keyboard()
            time.sleep(.001)

    def setup_udp(self):
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        self.sock.settimeout(0.1)
        self.sock.bind(("0.0.0.0", 5005))
        self.backend_addr = None
    
    def process_udp(self):
        try:
            data, addr = self.sock.recvfrom(5000)
            
            if self.backend_addr == None:
                self.backend_addr = addr

            update = json.loads(data)
            self.process_track_update(update)
            
        except KeyboardInterrupt:
            print("Bye")
            self.running = False
        except:
            pass

    def process_track_update(self, update):
        started_lanes = self.count_started_lanes(update['lanes'])
        play = started_lanes > 2
        if self.play_sounds != play:
            self.play_sounds = play
            if not play:
                self.play_yellow()
            elif self.flag == 'green':
                self.play_green()

        self.process_race_update(update['race'])
        self.process_lane_update(update['lanes'][self.lane-1])

    def count_started_lanes(self, lanes):
        started = 0
        for lane in lanes:
            if lane['started']:
                started = started + 1
        return started

    def process_race_update(self, update):
        if update['flag'] != self.flag:
            self.flag = update['flag']
            if self.flag == 'green' and self.play_sounds:
                self.play_green()
            else:
                self.play_yellow()

    def process_lane_update(self, update):
        #  {'lane': 8, 'best': 4.0, 'last': 10.0, 'laps': 163, 'pos': 1, 'started': True, 'name': '', 'color': 'green', 'state': 'go', 'pitinfo': '', 'pittime': 0, 'accident': False}
        if update['pos'] != self.pos:
            self.pos = update['pos']
            if self.pos == 1 and update['laps'] > 1:
                self.play_new_leader()

        if update['state'] != self.racer_state:
            self.racer_state = update['state']

            if self.racer_state == 'lgas':
                self.play_low_gas()
            if self.racer_state == 'out':
                self.play_out_gas()

        pitting = update['pittime'] > 0
        if pitting != self.pitting:
            self.pitting = pitting
            if pitting:
                self.play_pitting()

    def process_reader(self):
        try:
            result = self.scanner.read()
            if result:
                print(result)
                self.process_badge(result)
        except Exception as e:
            print(e)

    def process_badge(self, badge):
        if self.backend_addr:
            addr,port = self.backend_addr
            lane = self.lane-1
            url = f'http://{addr}/registration/lane/{lane}/badge_id'
            print(f'Register {badge} at {self.backend_addr}')
            r = requests.put(url, data=str(badge))
            print(r)
            print(r.content)
            self.play_welcome_sound()

    def setup_keyboard(self):
        import threading

        self.consoleBuffer = []

        def consoleInput(myBuffer):
            while True:
                myBuffer.append(input())
        
        threading.Thread(target=consoleInput, args=(self.consoleBuffer,), daemon=True).start() # start the thread

    def process_keyboard(self):
        if self.consoleBuffer:
            key = self.consoleBuffer.pop(0)
            if key == 'w':
                self.play_welcome_sound()
            if key == 'g':
                self.play_green()
            if key == 'y':
                self.play_yellow()
            if key == 'l':
                self.play_low_gas()
            if key == '1':
                self.play_new_leader()
            if key == 'p':
                self.play_pitting()
            if key == 'f':
                self.play_long_pitting()

    def setup_sound(self):
        mixer.pre_init(44100, -16, 1, 16)
        mixer.init()

        self.pit_sounds = [
            mixer.Sound('media/pit1.ogg'),
            mixer.Sound('media/pit2.ogg'),
            mixer.Sound('media/pit3.ogg'),
            mixer.Sound('media/pit4.ogg'),
        ]
        self.pass_sounds = [
            mixer.Sound('media/passes0.ogg'),
            mixer.Sound('media/passes1.ogg'),
            mixer.Sound('media/passes2.ogg')
        ]
        self.oog_sounds = [
            mixer.Sound('media/oog10.ogg'),
            mixer.Sound('media/oog20.ogg')
        ]
        self.low_gas_sounds = [
            mixer.Sound('media/oog21.ogg'),
            mixer.Sound('media/oog22.ogg')
        ]

    def play_welcome_sound(self):
        pass

    def play_random_sound(self, sounds):
        try:
            sound = random.choice(sounds)
            mixer.find_channel(True).play(sound, fade_ms=200)
        except:
            pass
        
    def play_new_leader(self):
        self.play_random_sound(self.pass_sounds)

    def play_pitting(self):
        self.play_random_sound(self.pit_sounds)

    def play_long_pitting(self):
        self.play_random_sound(self.pit_sounds)

    def play_low_gas(self):
        self.play_random_sound(self.low_gas_sounds)

    def play_out_gas(self):
        self.play_random_sound(self.oog_sounds)

    def play_green(self):
        if self.lane == 8:
            time.sleep(1)
            mixer.music.load('media/race.ogg')
            mixer.music.set_volume(0.2)
            mixer.music.play(loops=-1)
        if self.lane == 4:
            mixer.music.load('media/race.ogg')
            mixer.music.set_volume(0.2)
            mixer.music.play(loops=-1)

    def play_yellow(self):
        mixer.music.fadeout(2000)

station = RaceStation()
station.run()

