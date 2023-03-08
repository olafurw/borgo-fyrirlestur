import csv
import sys
import random
from dataclasses import dataclass

@dataclass
class Song:
    name: str = ''
    album: str = ''
    artists: str = ''
    track_number: int = 0
    explicit: bool = False
    danceability: float = 0.0
    energy: float = 0.0
    key: int = 0
    loudness: float = 0.0
    mode: int = 0
    speechiness: float = 0.0
    acousticness: float = 0.0
    instrumentalness: float = 0.0
    liveness: float = 0.0
    valence: float = 0.0
    tempo: float = 0.0
    duration_ms: int = 0
    time_signature: float = 0.0
    release_date: str = ''

def load_songs(filename):
    songs = []
    with open(filename, encoding='utf-8') as file:
        reader = csv.reader(file)
        for song in reader:
            s = Song(song[0], song[1], song[2],
                    int(song[3]), bool(song[4]), round(float(song[5]), 4), round(float(song[6]), 4),
                    int(song[7]), round(float(song[8]), 4), int(song[9]), round(float(song[10]), 4),
                    round(float(song[11]), 4), round(float(song[12]), 4), round(float(song[13]), 4), 
                    round(float(song[14]), 4), round(float(song[15]), 4), 
                    int(song[16]), round(float(song[17]), 4), song[18])
            songs.append(s)
    return songs
