from filechecker import *
from utils import run_as_thread

@run_as_thread()
def thread_inside_function():
    @on_file_changed(filename="test.txt")
    def inside_function():
        print("Change!!!")

@run_as_thread()
def thread_inside_function():
    @on_directory_changed()
    def inside_function(status: str, items: list):
        match status:
            case 'CREATE':
                print(f"We found created file: {items}")
            case 'DELETE':
                print(f"Oh on, file {items} was deleted")
            case 'REPLACE':
                print("You have problems...")

@run_as_thread()
def thread_inside_function():
    @on_processes_changed()
    def inside_function(status: str, items: list):
        match status:
            case 'CREATE':
                print(f"We found created process: {items}")
            case 'DELETE':
                print(f"Oh on, process {items} was deleted")
            case 'REPLACE':
                print("You have problems...")

@run_as_thread()
def thread_inside_function():
    @on_gpu_temperature_reached(goal=65, time=5)
    def inside_function():
        print("You need to cool down")

print("Write your code here")
