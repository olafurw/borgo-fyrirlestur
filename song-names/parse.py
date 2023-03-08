from songdb import load_songs
import csv

songs = load_songs('some_tracks.csv')

for song in songs:
    print(song)