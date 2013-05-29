# MusicMap

This is a very specific program I wrote to help me organize my music. 

It's purpose is to help you iterate through your artist folders. For each artist you can preview the songs, and then decide whether to do something to that artist or not. That something is what ever command you pass to the program as the second argument. The first argument is the location of your artist directories
## Assumptions

Your music should be in a layered directory structure like so `/<artist>/<album>/<title>`. There are many tools to help you organize your music like this based on tags.

This tool will skip empty folders.

## Example

In this example my artists are located in `/home/satshabad/Music/artists/` and I want to selectively remove artists. 

The `'%s'` is going to be the path to the artist I am currently on. (note the quotes so that paths with spaces work)

    python musicmap.py /home/satshabad/Music/artists/ "rm '%s'"

    Adam Green 
    size: 219.2 MB   files: 71       dirs: 5
     b : back
     p : preview 
    [s]: skip 
     d : do it 
    >

You are presented with a few choices. 

`b` will go back to the previous artist if you can.

`p` will start playing a song and give you a few preview options (see below).

`s` will skip to the next artist. It's also the default, so if you press enter, it will skip the artist.

`d` will apply whatever command to the artist folder under consideration

### Preview choices

    Adam Green 
    size: 219.2 MB   files: 71       dirs: 5
     n : next song 
     N : next album 
    [s]: skip 
     d : do it
    >

`s` and `d` are the same as above

`n` will play the next avaible track in the first subdirectory of your artist folder, when you have played every track it will start over with the first one
`N` will play the first track of the next subdirectory in your artist folder, when you have been through every subdir it will start over with the first one



