"""
8-8. User Albums: Start with your program from Exercise 8-7. Write a 
while loop that allows users to enter an album’s artist and title. 
Once you have that information, call make_album() with the user’s 
input and print the dictionary that’s created. Be sure to include a 
quit value in the while loop.
"""


def make_album(artist_name, album_title, number_song=None):
    album = {
        'Artist': artist_name.title(), 
        'Title': album_title.title()
        }
    if number_song:
        album['Number of Song'] = number_song
    return album


while True:
    print("\nPlease tell me the name of the artist: ")
    print("(enter 'q' at any time to quit!)")

    a_name = input("Artist name: ")
    if a_name == 'q':
        break
    a_title = input("Album name: ")
    if a_title == 'q':
        break
    print("If you know the number of song write it, if you don't, press Enter")
    n_song = input("Number of song: ")
    if n_song == 'q':
        break

    album = make_album(a_name, a_title, n_song)
    print(album)
