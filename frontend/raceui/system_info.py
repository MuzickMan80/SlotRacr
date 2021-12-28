from .ip_info import extract_ip
from ui.text_box import TextBox

class SystemInfo(TextBox):
    def __init__(self, rect, font):
        super().__init__(rect, font, text=extract_ip())