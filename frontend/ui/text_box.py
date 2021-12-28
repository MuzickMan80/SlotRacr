import pygame

class TextBox:
    def __init__(self, rect, font, text, fgColor=(0,0,86), bgColor=(182, 183, 185, 170), center=True):
        self.rect = pygame.Rect(rect)
        self.font = font
        self.text = text
        self.color = fgColor
        self.bgColor = bgColor
        self.center = center

    def draw(self,screen:pygame.Surface,fg):
        rects = []
        if fg:
            text_bmp = self.font.render(self.text, True, self.color)
            if self.center:
                text_rect = text_bmp.get_rect(center=(self.rect.centerx, self.rect.centery))
            else:
                text_rect = text_bmp.get_rect(topleft=(self.rect[0],self.rect[1]))

            screen.blit(text_bmp, text_rect)
            rects.append(text_rect)
        else:
            if self.bgColor:
                screen.fill(self.bgColor, self.rect)
                rects.append(self.rect)

        return rects