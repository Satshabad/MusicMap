import sys
import os
from subprocess import Popen, PIPE

from stuff import PathStats, Previewer

CMD = "mv '%s' /home/satshabad/Music/new_local"

def clear():
    os.system('cls' if os.name=='nt' else 'clear')

sys.stdin = open('/dev/tty')
proc = Popen('find /home/satshabad/Music/local  -maxdepth 1 -mindepth 1 -type d | sort', shell=True, stdin=PIPE, stdout=PIPE)

to_do_paths = list(reversed(proc.communicate()[0].split('\n')))
done_paths = []

while to_do_paths:
    path = to_do_paths.pop()
    
    stats = PathStats(path)

    if (not stats.num_of_files()) or (not all(ord(c) < 128 for c in path)):
        continue

    previewer = Previewer(path)

    clear()
    status_line = "%s \nsize: %s \t files: %s \t dirs: %s" % (stats.artist_name(), 
                                                               stats.folder_size(), 
                                                               stats.num_of_files(), 
                                                               stats.num_of_dirs())
    print status_line
    choice = raw_input(" b : back\n p : preview \n[s]: skip \n d : do it \n>")

    if choice == "p":

        previewer.start_preview()

        while choice != "d" and choice != "s" and choice != "":
            clear()
            print status_line

            choice = raw_input(" n : next song \n N : next album \n[s]: skip \n d : do it \n")

            if choice == "n":
                previewer.next_song()

            if choice == "N":
                previewer.next_album()


        previewer.stop_preview()


    if choice == "d":
        print "doing: ", CMD % path

        proc = Popen(CMD % path, shell=True, stderr=PIPE, stdout=PIPE)
        err, out = proc.communicate()

        if out or err:
            print out
            print err
    
        raw_input("done, press anything to continue...")
        done_paths.append(path)

    if choice == "b":
        to_do_paths.append(path)
        to_do_paths.append(done_paths.pop())

    if choice == "s" or choice == '':
        done_paths.append(path)

    clear()
