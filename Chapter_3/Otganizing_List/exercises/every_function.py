"""
3-10. Every Function: Think of things you could store in a list. For example, you
could make a list of mountains, rivers, countries, cities, languages, or anything
else you’d like. Write a program that creates a list containing these items and
then uses each function introduced in this chapter at least once.
"""

linux_os = ['ubuntu', 'fedora', 'debian', 'mint', 'zorin', 'kali', 'arch']
print(linux_os[1])
print(linux_os[-3])

print(linux_os[3].title())


print(linux_os.pop(0))
print(linux_os)

linux_os.append('kubuntu')
print(linux_os)


print(len(linux_os))


linux_os.reverse()
print(linux_os)

linux_os.sort()
print(linux_os)
