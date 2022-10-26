"""
4-11. My Pizzas, Your Pizzas: Start with your program from Exercise 4-1 (page 56).
Make a copy of the list of pizzas, and call it friend_pizzas. Then, do the
following:
• Add a new pizza to the original list.
• Add a different pizza to the list friend_pizzas.
• Prove that you have two separate lists. Print the message My favorite pizzas
are:, and then use a for loop to print the first list. Print the message My
friend’s favorite pizzas are:, and then use a for loop to print the second list.
Make sure each new pizza is stored in the appropriate list.
"""

my_pizzas = ['mexicana', 'pepperoni','hawaina']
friends_pizzas = my_pizzas[:]


my_pizzas.append('pastor')
friends_pizzas.append('doble queso')

print(my_pizzas)
print(friends_pizzas)

print(f"\nMy favorite pizza are {my_pizzas[0]}")

print("\n My pizza")
for my_pizza in my_pizzas:
    print(my_pizza)

print("\n Friends pizza")
for friend_pizza in friends_pizzas:
    print(friend_pizza)