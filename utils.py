import threading
from typing import Callable

def run_as_thread(*args: list, **kwargs: dict):
    def warpper(function: Callable):
        thread = threading.Thread(
            target = function,
            args = args,
            kwargs = kwargs
        )

        thread.start()
        return thread
    
    return warpper
