sudo apt update
set -e
#required crap
sudo apt install libssl-dev  -y
sudo apt install python3 python3-pip libffi-dev -y
sudo apt install -y libsqlite3-dev

if [ $1 == "audio" ]; then
	sudo apt install libopus0 ffmpeg
	sudo python3 -m pip install -U discord.py[voice] 
fi

sudo python3 -m pip install -U discord.py

#extra features: 
sudo pip3 install tinytag

#done
echo "Done."


