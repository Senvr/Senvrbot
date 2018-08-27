
#while true; do  sleep 1;        echo "1";       cat ~/pipy_bot/log.log; done &
cd ~/pipy_bot/


screen -A -m -d -S PyBot python3 ~/pipy_bot/main.py 

#while true; do  sleep 1;        echo "1";       cat ~/pipy_bot/log.log; done &


