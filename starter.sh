#AAA111
DIR="$( cd "$( dirname "${BASH_SOURCE[0]}" )">/dev/null && pwd)"
cd $DIR
cd ..
cp vFolder/SenvrBot1/main.py ./SenvrBot1/main.py
cp vFolder/SenvrBot1/starter.sh ./SenvrBot1/starter.sh
cd SenvrBot1
cp -R ./* ../vFolder/SenvrBot1
cd $DIR
screen -S SenvrBot1 -d -m python3 main.py
PID=$(cat pid)
