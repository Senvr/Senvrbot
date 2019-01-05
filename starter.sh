DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )" >/dev/null 2>&1 && pwd )"
cd $DIR
screen -S SenvrBotUNSTABLE -d -m python3 main.py
