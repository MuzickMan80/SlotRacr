import pygame, sys
import lane_table
import timer_socket

pygame.init()

try:
    dseg = pygame.font.Font('assets/DSEG7ModernMini-Bold.ttf', 60)

    default_font_name = pygame.font.get_default_font()
    header_font = pygame.font.SysFont(default_font_name, 50)

    size = width, height = 1368, 768
    screen_rect=(0,0,width,height)

    #screen = pygame.display.set_mode(size,pygame.FULLSCREEN|pygame.DOUBLEBUF|pygame.HWSURFACE)
    screen = pygame.display.set_mode(size)
    screen.set_alpha(None)

    bg = pygame.image.load("assets/background.png")
    bg = pygame.transform.smoothscale(bg, size)

    table = lane_table.LaneTable(size,dseg,header_font)

    tableBg = pygame.Surface(size, pygame.SRCALPHA)
    table.draw(tableBg,False)

    bgSurface = pygame.Surface(size)
    bgSurface.blit(bg, screen_rect)
    bgSurface.blit(tableBg, screen_rect)
    
    screen.blit(bgSurface, screen_rect)
    pygame.display.flip()

    foreground=pygame.Surface(size)
    foreground.blit(bgSurface, screen_rect)

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        lanes = timer_socket.get_lanes()
        table.update(lanes)

        rects = table.draw(foreground,True)
        for r in rects:
            screen.blit(foreground,r,r)
            foreground.blit(bgSurface,r,r)

        pygame.display.flip()
finally:
    timer_socket.disconnect()
