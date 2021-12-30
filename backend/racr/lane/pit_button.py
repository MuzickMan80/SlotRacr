
from racr.io.button import Button

class PitButton(Button):
    def __init__(self,io_manager,lane,pressed,down) -> None:
        try:
            super().__init__(io_manager,io_manager.get_pit_pin(lane-1),pressed,down)
        except Exception:
            pass
