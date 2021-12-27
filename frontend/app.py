#!/usr/bin/env python3
 
import pygame, sys
import argparse
import os
from lane_table import LaneTable
import timer_socket
from system_info import SystemInfo
import time
from GIFImage import GIFImage

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

    bg = pygame.image.load("assets/background.bmp")
    bg = pygame.transform.smoothscale(bg, size)

    dseg = pygame.font.Font('assets/DSEG7ModernMini-Bold.ttf', int(size[1]/18))
    default_font_name = pygame.font.get_default_font()
    header_font = pygame.font.SysFont(default_font_name, int(size[1]/20))

    pygame.mouse.set_visible(False)
    table = LaneTable(size,dseg,header_font)

    info_rect = (0,size[1]-30,size[0],30)
    info = SystemInfo(info_rect, header_font)

    tableBg = pygame.Surface(size, pygame.SRCALPHA)
    bgSurface = pygame.Surface(size)
    foreground=pygame.Surface(size)

    checkerboard = GIFImage('assets/checkered_flag.gif', size)
    
    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    pygame.quit()
                    
        lanes = timer_socket.get_lanes(args.target_ip)
        table.update(lanes)

        start = time.time()
        #bgSurface.blit(bg, screen_rect)
        checkerboard.render(bgSurface, screen_rect)

        table.draw(tableBg,False)
        bgSurface.blit(tableBg, screen_rect)
        
        #screen.blit(bgSurface, screen_rect)
        #pygame.display.flip()

        foreground.blit(bgSurface, screen_rect)

        rects = table.draw(foreground,True)
        rects.extend(info.draw(foreground,True))
        screen.blit(foreground, screen_rect)
        #for r in rects:
        #    screen.blit(foreground,r,r)
        #    foreground.blit(bgSurface,r,r)

        pygame.display.flip()
        update_time=time.time() - start
        #print(update_time)
finally:
    timer_socket.disconnect()
