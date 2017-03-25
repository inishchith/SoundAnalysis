#!/bin/bash

inp='n'

#checkmark hello
while [ $inp == 'n' ]
do
    say hello
    sleep 1
    python3 record.py
    say Did you say
    afplay test.wav

    echo "Is Recording ok? y/n "
    read inp
done

python3 extract_features.py
python3 detect.py

#rm -f output.wav right_output.wav
