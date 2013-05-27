import sys
import os
from os import walk
from subprocess import Popen
import subprocess

old_stdin = sys.stdin

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
        dev_null = open(os.devnull, 'w')
        print os.path.join(album_path, song_file_name)
        self.cvlc_proc = subprocess.Popen(['cvlc', "--quiet", os.path.join(album_path, song_file_name)], stdout=dev_null, stderr=dev_null)


    def play_next_album(self):
        self.current_album += 1
        self.current_song = -1
        self.play_next_song()

    def start_preview(self):
        self.play_next_album()
        choice = ""
        while not choice == "s":
            choice = raw_input("Enter s to skip artist, n for next song, N for next album, m for move\n")

            if choice == "n":
                self.play_next_song()

            if choice == "N":
                self.play_next_album()
        
        self.stop_preview()

    def stop_preview(self):
        self.cvlc_proc.terminate()


def no_songs(path):
    for root, subdirs, files in os.walk(path):
        if files:
            return False
    
    return True



path_to_artist = 1

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
    
