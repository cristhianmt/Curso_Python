"""
8-15. Printing Models: Put the functions for the example printing_models.py in a separate file called printing_functions.py. Write an import statement at the top of printing_models.py, and modify the file to use the imported functions.
"""

from models import print_models as pm, show_completed_models as scm


unprinted_designs = ['phone case', 'robot pendant', 'dodecahedron']
completed_models = []
# The slice notation [:] makes a copy of the list to send to the function. If
# we didn’t want to empty the list of unprinted designs
pm(unprinted_designs[:], completed_models)
scm(completed_models)