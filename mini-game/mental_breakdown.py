import os
import time
import sys
import lyricsgenius
from dotenv import load_dotenv

load_dotenv()

GENIUS_ACCESS_TOKEN = os.getenv("GENIUS_ACCESS_TOKEN")

def typewriter_print(text, delay=0.03):
    if not text:
        return
    
    clean_text = text.replace("Embed", "").strip()
    
    for char in clean_text:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(delay)
    print("\n" + "="*40)

def fetch_and_play(artist_name, song_title):
    if not GENIUS_ACCESS_TOKEN:
        print("Error: GENIUS_ACCESS_TOKEN not found in .env file.")
        return

    genius = lyricsgenius.Genius(GENIUS_ACCESS_TOKEN)
    genius.verbose = False
    genius.remove_section_headers = True

    print(f"Searching for '{song_title}' by {artist_name}...")
    
    try:
        song = genius.search_song(song_title, artist_name)
        
        if song:
            print(f"Found! Starting lyrics...\n")
            typewriter_print(song.lyrics)
        else:
            print(f"Could not find lyrics for '{song_title}'. Check the spelling!")
            
    except Exception as e:
        print(f"API Error: {e}")

if __name__ == "__main__":
    artist = "VIOLENT VIRA"
    track = "Commmon Decency"
    
    fetch_and_play(artist, track)