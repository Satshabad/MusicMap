# MusicMap

This is a very specific program I wrote to help me organize my music. 

It's purpose is to help you iterate through your artist folders in a /<artist>/<album>/<title> music directoy structure. For each artist you can preview the songs, and then decide whether to do something to that artist or not. That something is what ever command you pass to the program as the second argument. The first argument is the location of your artist directories

## examples

    python musicmap.py /home/satshabad/Music/artists/ "rm '%s'"

In this example my artists are located in `/home/satshabad/Music/artists/` and I want to selectivly remove artists. 

The `'%s'` is going to be the path to the artist I am currently on. (note the quotes so that paths with spaces work)
