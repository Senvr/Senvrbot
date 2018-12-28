sudo apt update
set -e
#required crap
sudo apt install libssl-dev  -y
sudo apt install python3 python3-pip libffi-dev -y
sudo apt install -y libsqlite3-dev
pip3 install thorn
sudo apt install libopus0 ffmpeg
sudo python3 -m pip install -U discord.py[voice] 
sudo python3 -m pip install -U discord.py
sudo pip3 install tinytag
echo "Done."
