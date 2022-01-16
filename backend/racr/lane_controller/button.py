import inspect

class Button:
    def __init__(self, lane_controller, lane, pressed_handler=None, down_handler=None, invert=False):
        self.pressed_handler = pressed_handler
        self.down_handler = down_handler
        self.pressed = not invert
        lane_controller.monitor_button(lane, self.on_pressed)

    async def on_pressed(self, edge):
        try:
            if self.pressed_handler and edge == self.pressed:
                result = self.pressed_handler()
                if inspect.isawaitable(result):
                    await result
            if self.down_handler:
                result = self.down_handler(edge == self.pressed)
                if inspect.isawaitable(result):
                    await result
        except Exception as ex:
            print(ex)
