import curses
from curses import wrapper, A_BOLD
from walkers import ArtistWalker
from walkers import ArtistPreviewer

def main(stdscr):
    artist_walker = ArtistWalker()
    while artist_walker.has_more_artists():
        artist_walker.move_to_next_artist()
        stdscr.addstr(artist_walker.get_current_artist_name(), A_BOLD)
        stdscr.refresh()
        previewer = ArtistPreviewer(artist_walker.get_current_artist_path())

        stdscr.move(1,0)

        stdscr.addstr("Enter s to skip artist, p to preview, n for next song, N for next album, m for move")
        choice = stdscr.getch()
        while choice != ord("s"):

            if choice == ord("p"):
                previewer.start_preview()

            if choice == ord("n"):
                previewer.play_next_song()

            if choice == ord("N"):
                previewer.play_next_album()

        previewer.stop_preview()
 
        stdscr.clear()

wrapper(main)
