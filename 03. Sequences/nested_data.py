albums = [
    ("Welcome to my Nightmare", "Alice Cooper", 1975,
     [
         (1, "Welcome to my Nightmare"),
         (2, "Devil's Food"),
         (3, "The Black Widow"),
         (4, "Some Folks"),
         (5, "Only Women Bleed"),
     ]
     ),
    ("Bad Company", "Bad Company", 1974,
     [
         (1, "Can't Get Enough"),
         (2, "Rock Steady"),
         (3, "Ready for Love"),
         (4, "Don't Let Me Down"),
         (5, "Bad Company"),
         (6, "The Way I Choose"),
         (7, "Movin' On"),
         (8, "Seagull"),
     ]
     ),
    ("Nightflight", "Budgie", 1981,
     [
         (1, "I Turned to Stone"),
         (2, "Keeping a Rendezvous"),
         (3, "Reaper of the Glory"),
         (4, "She Used Me Up"),
     ]
     ),
    ("More Mayhem", "Imelda May", 2011,
     [
         (1, "Pulling the Rug"),
         (2, "Psycho"),
         (3, "Mayhem"),
         (4, "Kentish Town Waltz"),
     ]
     ),
]

# for band, disc, year, songs in albums:
#     print('Band: {}, Disc: {}, Year: {}'.format(band, disc, year))
#     for index, song in songs:
#         print('\tTrack: {}, Name: {}'.format(index, song))


# going through the elements
# complete album
album = albums[2]
print(album)
# list of songs
songs = album[3]
print(songs)
# one particular song
song = songs[2]
print(song)
# song name
song_name = song[1]
print(song_name)

# all in one go, searching for the song "mayhem"
mayhem = albums[3][3][2][1]
print(mayhem)


