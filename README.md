# rekordbox-cue-points
A python script to automate setting rekordbox cue points.

This was inspired by Bide (https://github.com/Bide-UK, https://www.instagram.com/bide_uk/) and his rekodbox autocuer for Mac -> https://github.com/Bide-UK/Bides-Rekordbox-AutoCuer

The purpose of this program is to automatically set cue points for every track in a rekordbox playlist. Currently, the program sets cue points at bars 1,9,16,32,49,65,81 and 97.

## How to use
- Open Rekordbox, obviously...
- Create a playlist with all the tracks you need to add cue points to
- Make sure all the tracks have been analysed and that the bars are aligned with the track
- Set Rekordbox to Export - 1 Player mode
- Run the python script
- Type in the number of songs in the playlist
- Click on Rekordbox and press F1 when you're ready!

## Current To-Dos
- Make it easy for the user to customise the bars that the cue points are placed at - Currently, the code logic doesn't really allow for any customisation. It's just 1,9, and then it i multiples of 16
- Find a better way to make the script start - F1 is fine, but worst case someone could have that bound to something in rkbox and mess up the process
- Make the code look nicer (It works but it looks pretty shocking)