#!/bin/bash
echo "cloning github repo files..."
git clone https://github.com/29LHR/StockTrack.git
cd ./StockTrack

echo "adding .venv (Package manager)..."
python3 -m venv .venv
source .venv/bin/activate

echo "installing dependencies using pip..."
pip3 install --upgrade pip
pip3 install -r requirements.txt

echo "running setup wizard..."
python3 setup.py

echo "finished"
echo "to start use command:"
echo "source .venv/bin/activate && python3 main.py"

echo "deleting setup files..."
rm setup.py
cd ..
rm setup.sh

echo "starting app"
cd StockTrack
python3 main.py