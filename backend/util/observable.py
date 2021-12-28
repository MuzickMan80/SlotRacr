import inspect

class Observable:
    def __init__(self,observer) -> None:
        self.observer = observer    
    async def notify_observer(self):
        result = self.observer()
        if inspect.isawaitable(result):
            await result
