from filechecker import (
    on_directory_changed,
    on_file_changed,
    on_progress_changed
)

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
