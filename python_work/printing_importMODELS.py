# All the ways to import modules and functions...
import printing_models
from printing_models import print_models
from printing_models import print_models as pm
import printing_models as p
from printing_models import *


# Lets call the modules and functions!
unprinted_designs = ['iphone case', 'robot pendant', 'dodecahedron']
completed_models = []

pm(unprinted_designs, completed_models)
printing_models.show_completed_models(completed_models)

print_models(unprinted_designs, completed_models)
p.show_completed_models(completed_models)
# I already styled at least 3 of the functions and modules of the code for the entire 8th chapter.





# Practice and importing modules and functions along with styling functions frequently as it is an important practice.
# These are some ways to import functions and modules and print them. I already styled functions in other programs.