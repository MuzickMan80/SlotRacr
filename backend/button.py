import inspect

class Button:
    def __init__(self, io_manager, pin, handler):
        self.handler = handler
        io_manager.monitor_pin(pin, self.on_pressed, True)

    async def on_pressed(self, edge, tick):
        result = self.handler()
        if inspect.isawaitable(result):
            await result