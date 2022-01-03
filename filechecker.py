import os
import time

from typing import Callable

def _current_directory_items(path: str = None) -> list:
    return os.listdir(path) if path else os.listdir()

def _read_file_contents(path: str):
    with open(path, 'r', encoding='utf-8') as out:
        return out.read()

def on_directory_changed(**kwargs: dict):
    def warpper(function: Callable):
        ''' function(status: str, items: list) '''
        path = kwargs.get('path')
        current_items = _current_directory_items(path)

        while True:
            if current_items != (new := _current_directory_items(path)):
                items = list(set(current_items) ^ set(new))
                status = "CREATE" if len(current_items) < len(new) else "DELETE" if len(current_items) > len(new) else "REPLACE"

                function(status, items)
            
            current_items = new

            time.sleep(kwargs.get('time', 1))
    
    return warpper

def on_file_changed(**kwargs: dict):
    def warpper(function: Callable):
        if not (filename := kwargs.get('filename')):
            raise ValueError("filename must be specified")
        
        current_content = _read_file_contents(filename)

        while True:
            if current_content != (new := _read_file_contents(filename)):
                function()
            
            current_content = new

            time.sleep(kwargs.get('time', 1))
    
    return warpper
