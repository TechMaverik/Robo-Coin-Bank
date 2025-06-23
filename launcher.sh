#!/bin/bash

DIR=".robocoin"

if [ -d "$DIR" ]; then
    echo "The directory '$DIR' exists."
    source .robocoin/bin/activate
else
    echo "The directory '$DIR' does not exist."
    python3.10 -m venv .robocoin
    source .robocoin/bin/activate
    pip install -r requirements.txt
    

fi


python3 router.py
