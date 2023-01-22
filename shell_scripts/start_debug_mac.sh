#!/usr/bin/zsh

echo "Opening Ovation"
cd ..
pwd
code .

awhile=5

echo "Booting up dev environment"
source ovation_venv/bin/activate
sleep $awhile && open http://127.0.0.1:5000 & python main.py