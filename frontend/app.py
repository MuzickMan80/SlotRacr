#!/usr/bin/env python3
 
import pygame
import argparse
import traceback
from raceui.race_screen import RaceWindow
from ui.window import WindowManager

parser = argparse.ArgumentParser()
parser.add_argument('--target_ip', help='IP Address of the timer service', default='127.0.0.1')
parser.add_argument('--windowed', help='Run in windowed mode', action='store_true')

args = parser.parse_args()
pygame.init()

try:
    size = 1000, 500

    flags=0
    if args.windowed != True:
        flags = flags + pygame.FULLSCREEN
        size = 0, 0
    screen = pygame.display.set_mode(size,flags)
    screen.set_alpha(None)
    print(f'Driver: {pygame.display.get_driver()}')
    print(pygame.display.Info())

    size = screen.get_width(),screen.get_height()
    screen_rect=(0,0,screen.get_width(),screen.get_height())

    window_mgr = WindowManager(size)
    main = RaceWindow(window_mgr, args.target_ip)
    
    pygame.mouse.set_visible(False)
    running=True
    while running:
        window_mgr.draw(screen)
        pygame.display.flip()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running=False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    running=False
            else:
                window_mgr.event(event)
                 
    pygame.quit()
except Exception as e:
    f = open('exception.log','a')
    traceback.print_exc(file=f)
    f.close()
    traceback.print_exc()
    if running:
        pygame.quit()

    raise e
finally:
    main.cleanup()
