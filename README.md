# opened
A simple package adding some additional features to [open](https://docs.python.org/3/library/functions.html#open) handling folder creation if not existent. Allowing an extended option to return additional properties for writing tests. It also allows to change the root . directory thurder simplifying useage in tests in conjunction with [temporaryDirectory](https://docs.python.org/3/library/tempfile.html#tempfile.TemporaryDirectory).

# Usage

## Example without Extended
```py
    with opened('./', self.filename) as file:
        print(f"{file.read()}")
```

## Example with Extended
```py
    with opened('./', self.filename, extended=True) as file:
        print(f"{file.filehandle.read()}")
        print(f"{file.filepath}")
```

## Example with Temporary directory
```py
import tempfile
...
with tempfile.TemporaryDirectory() as temporary_directory:
    with opened('./', self.filename, extended=True, dot_root=temporary_directory) as file:
        print(f"{file.filepath}")
```

# Tests
## Windows
![Windows Python 3.7](https://github.com/rufreakde/opened/workflows/Windows%20Python%203.7/badge.svg?branch=master)  
![Windows Python 3.8](https://github.com/rufreakde/opened/workflows/Windows%20Python%203.8/badge.svg?branch=master)  
![Windows Python 3.9](https://github.com/rufreakde/opened/workflows/Windows%20Python%203.9/badge.svg?branch=master) 

## MacOS
![MAC Python 3.7](https://github.com/rufreakde/opened/workflows/MAC%20Python%203.7/badge.svg?branch=master)  
![MAC Python 3.8](https://github.com/rufreakde/opened/workflows/MAC%20Python%203.8/badge.svg?branch=master)  
![MAC Python 3.9](https://github.com/rufreakde/opened/workflows/MAC%20Python%203.9/badge.svg?branch=master)  

## Ubuntu
![Ubuntu Python 3.7](https://github.com/rufreakde/opened/workflows/Ubuntu%20Python%203.7/badge.svg?branch=master)  
![Ubuntu Python 3.8](https://github.com/rufreakde/opened/workflows/Ubuntu%20Python%203.8/badge.svg?branch=master)  
![Ubuntu Python 3.9](https://github.com/rufreakde/opened/workflows/Ubuntu%20Python%203.9/badge.svg?branch=master)  