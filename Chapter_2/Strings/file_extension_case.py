"""
2-8 File Extension: Python has a removesuffix() method that works exactly 
like removeprefix(). Assign the value 'python_notes.txt' to a variable called
filename. Then use the removesuffix() method to display without the file extension, like some file browser do. 
"""

file_name = 'python_notes.txt'
print(file_name.removeprefix('python'))
print(file_name.removesuffix('.txt'))