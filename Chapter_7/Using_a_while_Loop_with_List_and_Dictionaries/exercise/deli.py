"""
7-8. Deli: Make a list called sandwich_orders and fill it with the names of various
sandwiches. Then make an empty list called finished_sandwiches. Loop through
the list of sandwich orders and print a message for each order, such as I made
your tuna sandwich. As each sandwich is made, move it to the list of finished
sandwiches.After all the sandwiches have been made, print a message listing
each sandwich that was made. 
"""
sandwich_orders = ['veggie', 'grilled cheese', 'turkey', 'roast beef']
finished_sandwich = []
while sandwich_orders:
    current_sandwich = sandwich_orders.pop()
    print(f"I'm working on your {current_sandwich} sandwich.")
    finished_sandwich.append(current_sandwich)

for sandwich in finished_sandwich:
    print(f"I made your {sandwich} sandwich.")