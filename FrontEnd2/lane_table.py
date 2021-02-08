import pygame

width, height = 1368, 768
labels=['Lane','Laps','Top','Last']
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

class TableCell:
    def __init__(self, rect, bgcolor, font, color):
        self.rect=rect
        self.bgcolor=bgcolor
        self.text=''
        self.font=font
        self.color=color
        self.dirty=False
    def drawBg(self,screen):
        return pygame.draw.rect(screen,self.bgcolor, self.rect, 0, 20)
    def drawFg(self,screen):
        text_bmp = self.font.render(self.text, True, self.color)
        text_rect = text_bmp.get_rect(center=(self.rect.centerx,self.rect.centery))
        screen.blit(text_bmp, text_rect)
        return text_rect
    def draw(self,screen,fg):
        if fg:
            return self.drawFg(screen)
        else:
            return self.drawBg(screen)
    def update(self,label):
        if self.text != label:
            self.text = label
            self.dirty = True

class TableRow:
    def __init__(self, y, height, bgcolor, font, color):
        self.cells = []
        x=left
        for col in cols:
            area=pygame.Rect(x+margin,y+margin,col-margin*2,height-margin*2)
            self.cells.append(TableCell(area, bgcolor, font, color))
            x=x+col
    def draw(self,screen,fg):
        rects = []
        for cell in self.cells:
            if cell.dirty or not fg:
                rects.append(cell.draw(screen,fg))
                cell.dirty=not fg
        return rects
    def update(self,labels):
        for i in range(len(self.cells)):
            self.cells[i].update(labels[i])

class LaneTable:
    def __init__(self,size,dseg,header_font):
        self.headerRow = TableRow(top, headerHeight, headerBackground, header_font, headerColor)
        self.headerRow.update(labels)
        self.rows = []
        for row in range(numLanes):
            self.rows.append(TableRow(top+headerHeight+row*rowHeight, rowHeight, cellBackground, dseg, cellForeground))

    def draw(self,screen,fg):
        rects = []
        for row in self.rows:
            rects=rects + row.draw(screen,fg)
        if not fg:
            self.headerRow.draw(screen,False)
            self.headerRow.draw(screen,True)
        return rects

    def updateLane(self,lane,row):
        labels=[f'{lane["lane"]}',formatLaps(lane),formatTime(lane,lane['best']),formatTime(lane,lane['last'])]
        self.rows[row].update(labels)

    def update(self,lanes):
        row=0
        for lane in lanes:
            self.updateLane(lane,row)
            row=row+1
