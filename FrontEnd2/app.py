import pygame, sys
import socketio
import json

sio = socketio.Client()
sio.connect('http://192.168.1.74:5000')

lanes=[]

@sio.event
def update(data):
    global lanes
    lanes=json.loads(data)
    lanes.sort(key=lambda l: l['pos'])
    print(lanes)

pygame.init()

try:
    dseg = pygame.font.Font('DSEG7ModernMini-Bold.ttf', 60)

    default_font_name = pygame.font.get_default_font()
    header_font = pygame.font.SysFont(default_font_name, 50)

    size = width, height = 1368, 768
    speed = [2, 2]
    black = 0, 0, 0

    screen = pygame.display.set_mode(size)
    ''', flags=pygame.FULLSCREEN)'''

    bg = pygame.image.load("background.png")
    bg = pygame.transform.smoothscale(bg, size)
    ballrect = bg.get_rect()

    cols=[120,150,350,350]
    margin=2
    headerHeight=70
    numLanes=4
    rowHeight=100
    headerBackground=(182, 183, 185, 170)
    headerColor=(0,0,86)
    cellBackground=(0,0,86,128)
    cellForeground=(255,255,0)
    left=(width-sum(cols))/2
    top=(height-(headerHeight+numLanes*rowHeight))/2

    def drawCell(screen,rect:pygame.Rect,bgcolor,text,font,color):
        pygame.draw.rect(screen, bgcolor, rect, border_radius=20)
        text_bmp = font.render(text, True, color)
        text_rect = text_bmp.get_rect(center=(rect.centerx,rect.centery))
        screen.blit(text_bmp, text_rect)

    def drawRow(screen,y,height,bgcolor,texts,font,color):
        x=left
        col=0
        for text in texts:
            area=pygame.Rect(x+margin,y+margin,cols[col]-margin*2,height-margin*2)
            drawCell(screen, area, bgcolor, text, font, color)
            x=x+cols[col]
            col=col+1

    def drawHeader(screen):
        labels=['Lane','Laps','Top','Last']
        drawRow(screen, top, headerHeight, headerBackground, labels, header_font, headerColor)

    def formatTime(lane, time):
        if not lane['started']:
            return '!!!!!'
        elif time==None:
            return '-----'
        else:
            return pad(f'{time:0.3f}',6)

    def formatLaps(lane):
        if not lane['started']:
            return '---'
        else:
            laps=lane['laps']
            return pad(f'{laps}',3)

    def pad(text, width):
        while len(text) < width:
            text='!'+text
        return text

    def drawLane(screen,lane,row):
        labels=[f'{lane["lane"]}',formatLaps(lane),formatTime(lane,lane['best']),formatTime(lane,lane['last'])]
        drawRow(screen, top+headerHeight+row*rowHeight, rowHeight, cellBackground, labels, dseg, cellForeground)

    def drawTable(screen):
        drawHeader(screen)
        row=0
        for lane in lanes:
            drawLane(screen,lane,row)
            row=row+1

    def drawScreen(screen):
        screen.blit(bg, (0,0,width,height))
        overlay = pygame.Surface(size, pygame.SRCALPHA | pygame.HWSURFACE)
        drawTable(overlay)
        screen.blit(overlay, (0,0))

    while 1:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                sys.exit()

        drawScreen(screen)
        pygame.display.flip()

        sio.sleep(.03)
finally:
    sio.disconnect()