import sys
import os
from os import walk
import subprocess

class ArtistWalker():
    def __init__(self):
        dev_null = open(os.devnull, 'w')
        proc = subprocess.Popen('find "/media/satshabad/Black Beauty/Music/SelectedMusic" -maxdepth 1 -mindepth 1 -type d | sort | head -n 100', stdout=dev_null, stderr=dev_null, shell=True)

        self.artist_paths = proc.communicate()[0].split('\n')
        self.current_artist = -1


    def move_to_next_artist(self):
        self.current_artist += 1
        path_to_artist = self.artist_paths[self.current_artist]

        while self._no_songs(path_to_artist) and self.has_more_artists():
            self.current_artist += 1
            path_to_artist = self.artist_paths[self.current_artist]
    
    def get_current_artist_path(self):
        return self.artist_paths[self.current_artist]

    def get_current_artist_name(self):
        split_path = self.artist_paths[self.current_artist].split("/")
        artist = split_path[-1]
        return artist

    def has_more_artists(self):
        return self.current_artist < len(self.artist_paths)

    def _no_songs(self, path):
        for root, subdirs, files in os.walk(path):
            if files:
                return False
        
        return True


class ArtistPreviewer():
    def __init__(self, path):
        self.albums = list(walk(path))[1:]
        self.current_album = -1
        self.current_song = -1
        self.cvlc_proc = None
    
    def play_next_song(self):
        if self.cvlc_proc:
            self.stop_preview()

        self.current_song += 1
        album_path = self.albums[self.current_album % len(self.albums)][0]
        songs = self.albums[self.current_album % len(self.albums)][2]
        song_file_name = songs[self.current_song % len(songs)]
        self.cvlc_proc = subprocess.Popen(['cvlc', "--quiet", os.path.join(album_path, song_file_name)])
    
    def play_next_album(self):
        self.current_album += 1
        self.current_song = -1
        self.play_next_song()

    def start_preview(self):
        self.play_next_album()

    def stop_preview(self):
        self.cvlc_proc.terminate()

path_to_artist = 0

while path_to_artist:
    path_to_artist = sys.stdin.readline().strip('\n')
    if no_songs(path_to_artist):
        continue

    split_path =  path_to_artist.split("/")
    artist = split_path[-1]
    print artist
    sys.stdin = open('/dev/tty')
    choice = raw_input("enter p to play any song: ")

    if choice == 'p':
        artist_previewer = ArtistPreviewer(path_to_artist)
        artist_previewer.start_preview()

    sys.stdin = old_stdin
    
    
