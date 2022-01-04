# filechecker

directory
```python
@on_directory_changed(path="/path/to/directory", time=2)
def inside_function(status: str, items: list):
     ...
```

file
```python
@on_file_changed(filename="/path/to/file", time=2)
def inside_function():
    ...
```

process
```python
@on_progress_changed(time=2)
def inside_function(status: str, items: list):
    ...
```
gpu
```python
@on_gpu_temperature_reached(goal=65, time=5)
def inside_function():
    ...
```
