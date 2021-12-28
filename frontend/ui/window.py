import pygame

class Window:
    def __init__(self, mgr, visible:bool = True):
        self.visible = False
        self.mgr = mgr
        if visible:
            self.show()
    def show(self):
        if not self.visible:
            self.visible=True
            self.mgr.show(self)
    def hide(self):
        if self.visible:
            self.visible=False
            self.mgr.hide(self)
    def draw(self):
        pass
    def draw_background(self):
        pass

class WindowManager:
    def __init__(self, size):
        self.size = size
        self.windows: list[Window] = []
        self.fg_window = None
        self.bg_dirty = True
        WindowManager.instance=self

    def draw(self, screen) -> list[pygame.Rect]:
        rects = []
        for window in self.windows:
            rects.extend(window.draw(screen))
        return rects

    def draw_background(self, screen) -> list[pygame.Rect]:
        rects = []
        for window in self.windows:
            rects.extend(window.draw_background(screen))
        return rects

    def show(self, window: Window):
        self.windows.append(window)
    def hide(self, window: Window):
        self.windows.remove(window)
