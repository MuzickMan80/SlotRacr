import inspect
import asyncio

class Observable:
    def __init__(self,observer) -> None:
        self.observers = observer if isinstance(observer,list) else [observer]
    async def notify_observer_async(self):
        for observer in self.observers:
            result = observer()
            if inspect.isawaitable(result):
                await result
    def notify_observer(self):
        for observer in self.observers:
            result = observer()
            if inspect.isawaitable(result):
                asyncio.create_task(result)
    def add_observer(self,observer):
        self.observers.append(observer)
