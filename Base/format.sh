#!/bin/bash

inp='n'

#checkmark hello
while [ $inp == 'n' ]
do
    say hello
    sleep 1
    python3 Record.py
    say Did you say
    afplay output.wav

    echo "Is Recording ok? y/n "
    read inp
done

#python extract_feats.py right_output.wav

#rm -f output.wav right_output.wav
