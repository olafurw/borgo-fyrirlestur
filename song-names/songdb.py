import csv
from dataclasses import dataclass, field
from typing import List
from datetime import datetime, time

def release_to_date(release):
    if len(release) == 4 and release != '0000':
        return datetime.strptime(release, '%Y')
    elif len(release) == 7:
        return datetime.strptime(release, '%Y-%m')
    elif len(release) == 10:
        return datetime.strptime(release, '%Y-%m-%d')
    else:
        return datetime.strptime('1970-01-01', '%Y-%m-%d')

@dataclass
class Song:
    id: str = ''
    name: str = ''
    album: str = ''
    album_id: str = ''
    artists: List[str] = field(default_factory=list)
    artists_ids: List[str] = field(default_factory=list)
    track_number: int = 0
    disc_number: int = 0
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
    year: int = 0
    release_date: datetime = datetime(1970, 1, 1)

def load_songs(filename):
    songs = []
    with open(filename, encoding='utf-8') as file:
        next(file) # skips the first row

        reader = csv.reader(file)
        for song in reader:
            s = Song(song[0], song[1], song[2], song[3], song[4], song[5],
                    int(song[6]), int(song[7]), bool(song[8]), float(song[9]), float(song[10]),
                    int(song[11]), float(song[12]), int(song[13]), float(song[14]),
                    float(song[15]), float(song[16]), float(song[17]), float(song[18]),
                    float(song[19]), int(song[20]), float(song[21]), int(song[22]), release_to_date(song[23]))
            songs.append(s)
    return songs
