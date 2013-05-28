import os
import subprocess

dev_null = open('/dev/null', 'w')
class AlbumWalker():
    def __init__(self, path):
        self.path = path
        self.walk = [ w for w in os.walk(path) if w[2] ]

        self.current_album = 0
        self.current_song = 0 


    def next_song_path(self):
        songs = self.walk[self.current_album][2]
        song = songs[self.current_song]
        self.current_song = (self.current_song) + 1 % len(songs)
        return os.path.join(self.path, self.walk[self.current_album][0], song)


    def change_albums(self):
        self.current_album = (self.current_album + 1) % len(self.walk)
        self.current_song = 0


class Previewer():
    def __init__(self, path):
        self.cvlc_proc = None
        self.walker = AlbumWalker(path)

    def start_preview(self):
        self.next_song()

    def stop_preview(self):
        self.cvlc_proc.terminate()
        
    def next_song(self):
        if self.cvlc_proc:
            self.stop_preview()
        next_song_path = self.walker.next_song_path()

        self.cvlc_proc = subprocess.Popen(['cvlc', "--quiet", next_song_path], stdout=dev_null, stderr=dev_null)

    def next_album(self):
        self.walker.change_albums()
        self.next_song()

class PathStats():

    def __init__(self, path):
        self.path = path

    def artist_name(self):
        return self.path.split("/")[-1]

    def folder_size(self):
        total_size = 0
        for dirpath, dirnames, filenames in os.walk(self.path):
            for f in filenames:
                fp = os.path.join(dirpath, f)
                total_size += os.path.getsize(fp)
        return self._format_size(total_size)

    def _format_size(self, size):
        for x in ['bytes','KB','MB','GB']:
            if size < 1024.0:
                return "%3.1f %s" % (size, x)
            size /= 1024.0
        return "%3.1f %s" % (size, 'TB')

    def num_of_files(self):
        return sum(len(files) for root, dirs, files in os.walk(self.path))



    def num_of_dirs(self):
        return len([name for name in os.listdir(self.path)
            if os.path.isdir(os.path.join(self.path, name))])


