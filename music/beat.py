# beats per min goes here
#from __future__ import print_function

import librosa

import librosa


#add default location here
filename = 'train/edmtest.mp3'

y, s = librosa.load(filename)

temp, frames = librosa.beat.beat_track(y=y, sr=s)

print('Estimated tempo: {:.2f} beats per minute'.format(temp))

bpm = librosa.frames_to_time(frames, sr=s)

print('Saving output to bpm.csv')
#librosa.output.times_csv('bpm.csv', bpm)