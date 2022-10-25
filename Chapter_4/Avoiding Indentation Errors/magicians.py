"""
Sometimes your loop will run without any errors but won’t produce the
expected result. This can happen when you’re trying to do several tasks
in a loop and you forget to indent some of its lines.
For example, this is what happens when we forget to indent the second
line in the loop that tells each magician we’re looking forward to their next
trick:
"""
magicians = ["alice", 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick! ")
print(f"I can't wait to see your next trick, {magician.title()}")


"""
Indenting Unnecessarily
If you accidentally indent a line that doesn’t need to be indented, Python
informs you about the unexpected indent:
"""

# message = "Hello Python world!"
# print(message)

"""
Indenting Unnecessarily After the Loop
If you accidentally indent code that should run after a loop has finished,
that code will be repeated once for each item in the list. Sometimes this
prompts Python to report an error, but often this will result in a logical
error.
For example, let’s see what happens when we accidentally indent the
line that thanked the magicians as a group for putting on a good show:
"""

print("\n Indenting Unnecessarily after the loop")
magicians = ['alice', 'david', 'carolina']
for magician in magicians:
    print(f"{magician.title()}, that was a great trick!")
    print(f"I can't wait to see your next trick, {magician.title()}.\n")
    
    print("Thank you everyone, that was a great magic show!")


