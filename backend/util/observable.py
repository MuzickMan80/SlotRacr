import inspect
import asyncio

class Observable:
    def __init__(self,observer) -> None:
        self.observer = observer    
    async def notify_observer_async(self):
        result = self.observer()
        if inspect.isawaitable(result):
            await result
    def notify_observer(self):
        result = self.observer()
        if inspect.isawaitable(result):
            asyncio.create_task(result)