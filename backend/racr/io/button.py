import inspect

class Button:
    def __init__(self, io_manager, pin, pressed_handler=None, invert=True):
        self.pressed_handler = pressed_handler
        self.pressed = not invert
        io_manager.monitor_pin(pin, self.on_pressed, 
            rising=True, falling=True, pullUp=invert, pullDown=not invert, filterUs=10000)

    async def on_pressed(self, edge, tick):
        if self.pressed_handler and edge == self.pressed:
            result = self.pressed_handler()
            if inspect.isawaitable(result):
                await result