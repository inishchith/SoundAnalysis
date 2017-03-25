# to do
#!/bin/bash

inp='y'

#checkmark hello
while [ $inp == 'y' ]
do
    say hello
    sleep 1
    python3 test.py
    python3 detect.py

    echo "Wanna test more (y/n) ?"
    read inp
done

#python extract_feats.py right_output.wav

#rm -f output.wav right_output.wav
