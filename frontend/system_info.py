from ip_info import extract_ip

class SystemInfo:
    def __init__(self, rect, font):
        self.rect = rect
        self.font = font
        self.text = extract_ip()
        self.color = (182, 183, 185, 0)

    def draw(self,screen,fg):
        rects = []
        if fg:
            text_bmp = self.font.render(self.text, True, self.color)
            text_rect = text_bmp.get_rect(topleft=(self.rect[0]+20,self.rect[1]))
            screen.blit(text_bmp, text_rect)
            rects.append(text_rect)
        
        return rects