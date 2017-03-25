#!/bin/bash

inp='y'

#checkmark hello
while [ $inp == 'y' ]
do
    sleep 1
    python3 test.py
    afplay output.wav
    python3 detect.py
    echo "do yo want to test some more ? (y/n) "
    read inp
done

#python extract_feats.py right_output.wav

#rm -f output.wav right_output.wav
