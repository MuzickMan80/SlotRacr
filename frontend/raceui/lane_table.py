import pygame

numLanes=8
labels=['Status','Lane','Car','Laps','Top','Last']
headerBackground=(182, 183, 185, 170)
headerColor=(0,0,86)
cellBackground=(0,0,86,128)
cellForeground=(255,255,0)

class TableDims:
    def __init__(self, size):
        self.origWidth=1920
        self.origHeight=1080
        self.size = size
        self.cols=[
            self.scale(200),
            self.scale(180),
            self.scale(350),
            self.scale(200),
            self.scale(350),
            self.scale(350)
            ]
        self.margin=self.scale(2)
        self.headerHeight=self.scale(70)
        self.rowHeight=self.scale(100)
        self.cellCornerRadius=self.scale(20)
        self.left=(self.size[0]-sum(self.cols))/2
        self.top=(self.size[1]-(self.headerHeight+numLanes*self.rowHeight))/2

    def scale(self, dim):
        return int(round(dim / self.origWidth * self.size[0]))

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
    def __init__(self, rect, bgcolor, font, color, round):
        self.rect=rect
        self.bgcolor=bgcolor
        self.text=''
        self.font=font
        self.color=color
        self.dirty=False
        self.round=round
    def drawBg(self,screen):
        return pygame.draw.rect(screen, self.bgcolor, self.rect)
    def drawFg(self,screen):
        text_bmp = self.font.render(self.text, True, self.color)
        text_rect = text_bmp.get_rect(center=(self.rect.centerx,self.rect.centery))
        screen.blit(text_bmp, text_rect)
        return self.rect
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
    def __init__(self, dims, y, height, bgcolor, font, color):
        self.cells = []
        x=dims.left
        for col in dims.cols:
            area=pygame.Rect(x+dims.margin,y+dims.margin,col-dims.margin*2,height-dims.margin*2)
            self.cells.append(TableCell(area, bgcolor, font, color, dims.cellCornerRadius))
            x=x+col
        
        left = self.cells[3].rect.left
        width = self.cells[-1].rect.right - left
        area=pygame.Rect(left,y+dims.margin,width,height-dims.margin*2)
        self.pit_info_cell = TableCell(area, bgcolor, font, color, dims.cellCornerRadius)
        self.pit_info = ''

    def draw(self,screen,fg):
        rects = []
        if self.pit_info:
            for cell in self.cells[:3]:
                if cell.dirty or not fg:
                    rects.append(cell.draw(screen,fg))
                    cell.dirty=not fg
            if self.pit_info_cell.dirty or not fg:
                rects.append(self.pit_info_cell.draw(screen,fg))
                self.pit_info_cell.dirty=not fg
        else:
            for cell in self.cells:
                if cell.dirty or not fg:
                    rects.append(cell.draw(screen,fg))
                    cell.dirty=not fg
        return rects
    def update(self,labels,pitinfo=''):
        for i in range(len(self.cells)):
            self.cells[i].update(labels[i])
            
        self.pit_info = pitinfo
        self.pit_info_cell.update(pitinfo)

class LaneTable:
    def __init__(self,size,dseg,header_font,text_font,pit_info_font):
        self.size = size
        self.dims = dims = TableDims(size)
        self.headerRow = TableRow(dims, dims.top, dims.headerHeight, headerBackground, header_font, headerColor)
        self.headerRow.update(labels)
        self.rows = []
        for row in range(numLanes):
            row = TableRow(dims, dims.top+dims.headerHeight+row*dims.rowHeight, dims.rowHeight, cellBackground, dseg, cellForeground)
            row.cells[0].font = text_font
            row.cells[2].font = text_font
            row.pit_info_cell.font = pit_info_font
            self.rows.append(row)

    def draw(self,screen,fg):
        rects = []
        for row in self.rows:
            rects=rects + row.draw(screen,fg)
        if not fg:
            self.headerRow.draw(screen,False)
            self.headerRow.draw(screen,True)
        return rects

    def updateLane(self,lane,row):
        labels=[lane["state"],f'{lane["lane"]}',lane["name"],formatLaps(lane),formatTime(lane,lane['best']),formatTime(lane,lane['last'])]
        self.rows[row].update(labels,lane["pitinfo"])

    def update(self,lanes):
        row=0
        for lane in lanes["lanes"]:
            self.updateLane(lane,row)
            row=row+1
