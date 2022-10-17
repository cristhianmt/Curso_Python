"""when working with strings, another common task is to remove a prefix. 
Considers URL with the common prefix https://. We wanted to remove this prefix, so we can 
focus on just the part of the URL that users need to enter into an address bar
"""
nostarch_url = 'https://nostarch.com'
print(nostarch_url.removeprefix('https://'))

print("\n")
simple_url = nostarch_url.removeprefix('https://')
print(simple_url)

"""
When you se a URL in an address bar and the https:// part isnt shown, 
the browser is probably using a method like removeprefix() behind the scenes
"""