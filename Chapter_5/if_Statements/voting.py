"""
if Statements
When you understand conditional tests, you can start writing if statements.
Several different kinds of if statements exist, and your choice of which to
use depends on the number of conditions you need to test. You saw several
examples of if statements in the discussion about conditional tests, but now
let’s dig deeper into the topic.
Simple if Statements
The simplest kind of if statement has one test and one action:
"""

age = 19
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")


print("\n")
age = 17
if age > 18:
    print("You are old enough to vote!")
    print("Have you registered to vote yet?")
else:
    print("Sorry, you are to young to vote.")
    print("Please register to vote as soon as you turn 18!")
