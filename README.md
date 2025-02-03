# # Python Script Line Counter

## Description
This script counts the number of non-empty, non-comment lines in a specified Python file.

## Usage
python script.py filename.py

### Requirements
- Python 3.x
- The script should be run from the command line.
- A valid Python file (`.py`) must be provided as an argument.

## Features
- Removes empty lines.
- Ignores lines that start with `#` (comments).
- Prints the number of valid code lines.
- Provides error handling for missing arguments and incorrect file types.

## Error Handling
- If no filename is provided, the script will display an error message and exit.
- If a non-Python file is provided, it will notify the user.
- Catches unexpected errors and provides a meaningful error message.

## Example
Given a file `example.py` with the following content:
```python
# This is a comment

def hello():
    print("Hello, world!")  # This prints a message

hello()
```

Running:
python script.py example.py

Will output:
2

(Since it ignores the comment and empty line)

## License
This script is free to use and modify.

