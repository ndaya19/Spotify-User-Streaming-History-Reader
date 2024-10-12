import json
import os
from datetime import datetime

THRESHOLD_MS = 30000

directory = './'
cutoff_date = datetime(2023, 12, 31)
items_to_display = 10
lifetime = False

song_counts = {}
artist_playtime = {}
artist_play_counts = {}

last_played_song = None
for filename in os.listdir(directory):
    if filename.endswith(".json"):
        # Open and read the JSON file
        with open(os.path.join(directory, filename), 'r', encoding='utf-8') as f:
            data = json.load(f)
        
        for entry in data:
            artist = entry["artistName"]
            track = entry["trackName"]
            ms_played = entry["msPlayed"]
            end_time_str = entry["endTime"]

            end_time = datetime.strptime(end_time_str, "%Y-%m-%d %H:%M")

            current_song = f"{artist} - {track}"

            # Check if the track was played for longer than 30 seconds and after the cutoff date and isn't the same song as the previous
            if ((lifetime == True) or (lifetime == False and end_time >= cutoff_date)) and ms_played > THRESHOLD_MS and artist != "Unknown Artist" and current_song != last_played_song:
                hrs_played = ms_played / 1000 / 60 / 60
                # Update artist playtime
                if artist in artist_playtime:
                    artist_playtime[artist] += hrs_played
                else:
                    artist_playtime[artist] = hrs_played

                # Update artist play counts
                if artist in artist_play_counts:
                    artist_play_counts[artist] += 1
                else:
                    artist_play_counts[artist] = 1

                # Update song play counts
                if current_song in song_counts:
                    song_counts[current_song] += 1
                else:
                    song_counts[current_song] = 1

            last_played_song = current_song

print(f"\nTop {items_to_display} artists by hours")
artist_playtime = sorted(artist_playtime.items(), key=lambda x: x[1], reverse=True)
for artist, total_hrs in artist_playtime[:items_to_display]:
    print(f"{artist}: {total_hrs:.2f} hrs")

print(f"\nTop {items_to_display} artists by play count")
artist_play_counts = sorted(artist_play_counts.items(), key=lambda x: x[1], reverse=True)
for artist, count in artist_play_counts[:items_to_display]:
    print(f"{artist}: {count} plays")

print(f"\nTop {items_to_display} songs")
song_counts = sorted(song_counts.items(), key=lambda x: x[1], reverse=True)
for song, count in song_counts[:items_to_display]:
    print(f"{song}: {count} plays")



