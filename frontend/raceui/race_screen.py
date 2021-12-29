import pygame
from ui.text_box import TextBox
from ui.window import Window, WindowManager
from ui.GIFImage import GIFImage
from raceui.lane_table import LaneTable
from raceui.system_info import SystemInfo
import timer_socket
import time

class RaceWindow(Window):
    def __init__(self,mgr:WindowManager,target_ip):
        super().__init__(mgr)
        self.target_ip = target_ip
        self.size = mgr.size
        size = self.size
        
        bg = pygame.image.load("assets/background.bmp")
        self.bg = pygame.transform.smoothscale(bg, size)

        dseg = pygame.font.Font('assets/DSEG7ModernMini-Bold.ttf', int(size[1]/18))
        default_font_name = pygame.font.get_default_font()
        header_font_size = int(size[1]/20)
        header_font = pygame.font.SysFont(default_font_name, header_font_size)
        
        self.table = LaneTable(size,dseg,header_font)

        info_h = header_font_size * 1.2
        info_w = header_font_size * 8
        info_x = 10
        info_y = size[1]-info_h
        info_rect = (info_x,info_y,info_w,info_h)
        self.info = SystemInfo(info_rect, header_font)

        fps_x = info_x + info_w + 10
        fps_w = header_font_size * 3
        fps_rect = (fps_x, info_y, fps_w, info_h)
        self.fps = TextBox(fps_rect, header_font, "")

        self.tableBg = pygame.Surface(size, pygame.SRCALPHA)
        self.bgSurface = pygame.Surface(size)
        self.foreground=pygame.Surface(size)

        self.checkerboard = GIFImage('assets/checkered_flag.gif', size)

    def cleanup(self):
        timer_socket.disconnect()

    def draw(self, screen):
        start = time.time()
        
        lanes = timer_socket.get_lanes(self.target_ip)
        self.table.update(lanes)

        screen_rect=(0,0,self.size[0],self.size[1])
        self.bgSurface.blit(self.bg, screen_rect)
        #self.checkerboard.render(self.bgSurface, screen_rect)

        self.table.draw(self.tableBg,False)
        self.info.draw(self.tableBg,False)
        self.fps.draw(self.tableBg,False)
        self.bgSurface.blit(self.tableBg, screen_rect)
        
        #screen.blit(bgSurface, screen_rect)
        #pygame.display.flip()

        self.foreground.blit(self.bgSurface, screen_rect)

        rects = self.table.draw(self.foreground,True)
        rects.extend(self.info.draw(self.foreground,True))
        rects.extend(self.fps.draw(self.foreground,True))

        screen.blit(self.foreground, screen_rect)
        #for r in rects:
        #    screen.blit(foreground,r,r)
        #    foreground.blit(bgSurface,r,r)

        update_time=time.time() - start

        self.fps.text = str(round(update_time*1000))
        #print(update_time)
        return rects

