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
        bg = pygame.transform.smoothscale(bg, size)

        dseg = pygame.font.Font('assets/DSEG7ModernMini-Bold.ttf', int(size[1]/18))
        default_font_name = pygame.font.get_default_font()
        header_font = pygame.font.SysFont(default_font_name, int(size[1]/20))
        
        self.table = LaneTable(size,dseg,header_font)

        info_y = size[1]-30
        info_rect = (10,info_y,130,30)
        self.info = SystemInfo(info_rect, header_font)

        fps_rect = (150, info_y, 40, 30)
        self.fps = TextBox(fps_rect, header_font, "")

        self.tableBg = pygame.Surface(size, pygame.SRCALPHA)
        self.bgSurface = pygame.Surface(size)
        self.foreground=pygame.Surface(size)

        self.checkerboard = GIFImage('assets/checkered_flag.gif', size)

    def __del__(self):
        timer_socket.disconnect()

    def draw(self, screen):
        start = time.time()
        
        lanes = timer_socket.get_lanes(self.target_ip)
        self.table.update(lanes)

        screen_rect=(0,0,self.size[0],self.size[1])
        #bgSurface.blit(bg, screen_rect)
        self.checkerboard.render(self.bgSurface, screen_rect)

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

