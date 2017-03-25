# exracting faetures

"""
version:
Read doc - https://librosa.github.io/librosa/install.html#pypi

Terminlogy :
    sr = sampling rate ( default : 22050 hz)
    frame = short audio clip / snippet
    n_fft = No of samples per audio frame ( 2048 )
    hop_lenght : samples between frames ( 512 )

use - Freesounds.org -> .wav
to-add matplotlib

"""

import  sklearn
import timeit
import  matplotlib
import numpy as np
import librosa.display

# Load from dir - .wav file : , init example
# dir = train/cats .mp3 train/dogs .mp3

#version count
start= 0
stop = 10
data=['divya','prafful','ahaan','nishchith','pravar']

st = timeit.default_timer()
for name in data:
    for v in range(start,stop):
        for j in range(0,5):
            # dir here
            y, sr = librosa.load('train/' + name + '/' + str(v)+'_'+str(j) + '.wav')
            hop = 512
            harmonic, percussive = librosa.effects.hpss(y)

            tempo, beat_frames = librosa.beat.beat_track(y=y,
                                                         sr=sr)
            mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop, n_mfcc=13)

            mfcc_delta = librosa.feature.delta(mfcc)

            beat_mfcc_delta = librosa.display.util.sync(np.vstack([mfcc, mfcc_delta]), beat_frames)

            chromagram = librosa.feature.chroma_cqt(y=harmonic,
                                                    sr=sr)
            beat_chroma = librosa.display.util.sync(chromagram,
                                                    beat_frames,
                                                    aggregate=np.median)
            beat_features = np.vstack([beat_chroma, beat_mfcc_delta])

            transpose = beat_features.transpose()

            # output dir -  mono/animal-name
            # saving as .mfcc files
            # saving numpy.nd in output.mfcc
            # remember to extract only [1st , middle , last]
            # now i have rows = 38 , column = dependencies on duration
            # print(transpose)
            output = "train/" + name + '_m/' + str(v)+'_'+str(j) + '.mfcc'
            data = np.vstack([transpose[1], transpose[len(transpose) // 2], transpose[len(transpose) - 2]])
            data = np.transpose(data)
            np.savetxt(output, data)
    print("done with "+name)

sp=timeit.default_timer()
print("time taken = ",(sp-st))