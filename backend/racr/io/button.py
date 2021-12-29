import inspect

class Button:
    def __init__(self, io_manager, pin, pressed_handler=None, down_handler=None, invert=True):
        self.pressed_handler = pressed_handler
        self.down_handler = down_handler
        self.pressed = not invert
        io_manager.monitor_pin(pin, self.on_pressed, rising=True, falling=True, pullUp=invert, pullDown=not invert)

    async def on_pressed(self, edge, tick):
        if self.pressed_handler and edge == self.pressed:
            result = self.pressed_handler()
            if inspect.isawaitable(result):
                await result
        if self.down_handler:
            result = self.down_handler(edge == self.pressed)
            if inspect.isawaitable(result):
                await result