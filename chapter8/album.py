music_dictionary = {}

def make_album(artist, album, tracknum = ''):
    music = {'artist': artist, 'album': album}
    if tracknum:
        music['track_number'] = tracknum
    return music

while True:
    musician = input("Who is the musician?: ")
    album = input("What is the album?: ")
    tracknum = input("How many tracks are there?: ")
    if musician == '':
        break
    music_info = make_album(musician, album, tracknum)
    print(music_info)