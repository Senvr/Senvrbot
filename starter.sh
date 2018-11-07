DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )">/dev/null && pwd)"
echo $DIR
cd $DIR
screen -S SenvrBot1 -d -m python3 main.py
PID=$(cat pid)
