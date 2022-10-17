"""
2-7 Use a variable to represent a person's name, and include some whitespace characters at the beginning 
and end of the name. 
make sure you use each character combination, "\t" and "\n", at least once. 

print the name once, so the white space around the name is displayed. 
then print the name using each of the three stripping functions, lstrip(). rstrip(), and strip()
"""

from time import perf_counter, process_time_ns


person_name = " \t\n Sharon white "
print(person_name)
print(person_name.lstrip())
print(person_name.rstrip())
print(person_name.strip())
