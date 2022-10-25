"""
We begin by defining a list, just as we did in Chapter 3. Then we define
a for loop. This line tells Python to pull a name from the list magicians,
and associate it with the variable magician. Next, we tell Python to print the
name that’s just been assigned to magician. Python then repeats these last
two lines, once for each name in the list. It might help to read this code as
“For every magician in the list of magicians, print the magician’s name.”
The output is a simple printout of each name in the list:
"""
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(magician)

print("\n")

magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}\n")

print("Thank you, everyone. That was a great magic show!")