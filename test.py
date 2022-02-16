
{
    "cmd": ["C:/Python310/python.exe", "-u", "$file"],
    "file_regex": "^[ ]*File \"(...*?)\", line ([0-9]*)",
    "selector": "source.python",
    "env":{"PYTHONIOENCODING":"utf8"}
}
print('Hello world')
import sys
print(sys.version)
#