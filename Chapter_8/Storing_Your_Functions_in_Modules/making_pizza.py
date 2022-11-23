"""
Now we’ll make a separate file called making_pizzas.py 
in the same directory as pizza.py. This file imports the module 
we just created and then makes two calls to make_pizza():
"""

import pizza

pizza.make_pizza(16, 'pepperoni')
pizza.make_pizza(12, 'mushrooms', 'green peppers',
                 'green peppers', 'extra cheese')
