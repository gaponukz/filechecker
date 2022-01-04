from filechecker import *

@on_file_changed(filename="test.txt")
def inside_function():
    print("Change!!!")

@on_directory_changed()
def inside_function(status: str, items: list):
    match status:
        case 'CREATE':
            print(f"We found created file: {items}")
        case 'DELETE':
            print(f"Oh on, file {items} was deleted")
        case 'REPLACE':
            print("You have problems...")

@on_progress_changed()
def inside_function(status: str, items: list):
    match status:
        case 'CREATE':
            print(f"We found created process: {items}")
        case 'DELETE':
            print(f"Oh on, process {items} was deleted")
        case 'REPLACE':
            print("You have problems...")

@on_gpu_temperature_reached(goal=65, time=5)
def inside_function():
    print("You need to cool down")
