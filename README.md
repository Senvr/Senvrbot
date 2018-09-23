# <h1>Senvrbot</h1>
My Discord bot written in Python via discord.py
NOTE: You will need to enter your own discord bot token in. I assume you know how to do that.
## Quotes.txt
Quotes are read from `quotes.txt` found in the root path

## Audio/
Audio is read from the directory listing of the `audio` directory, a random track in said directory is played 

## install.sh
A shell script that installs the required dependancies. Tested and works on Ubuntu 18.04, Debian 9. Should work on a raspberry pi or something but I'm not 100% on that
## startup.sh
Shell script that starts the application in a screen session. You can start the bot directly via `python3 main.py`.

## pid(file)
dynamic PID file

# <h1>Commands</h1>
### ping
return a message. used to check if the bot is working or not

### quoteadd
add a quote to the quotes file

### quote
display a random line from the file

### phrase
display a random phrase from an array

### image
display a random phrase and image

### play
plays a random sound effect from the audio directory

### react
not finished

### pid
display  pid

### isup
see if a process is running on the host OS

### getreactions
unfinished

### github
post github link
