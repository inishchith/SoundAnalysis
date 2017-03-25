# exracting faetures

"""

Read doc - https://librosa.github.io/librosa/install.html#pypi

Terminlogy :
    sr = sampling rate ( default : 22050 hz)
    frame = short audio clip / snippet
    n_fft = No of samples per audio frame ( 2048 )
    hop_lenght : samples between frames ( 512 )

use - Freesounds.org -> .wav

"""
import  sklearn
import  matplotlib
import numpy as np
import librosa.display

# Load from dir - .wav file : , init example

y, sr = librosa.load('test.wav')

hop = 512

# components
harmonic,percussive = librosa.effects.hpss(y)

tempo, beat_frames = librosa.beat.beat_track(y=y,
                                             sr=sr)

# Compute mfcc features from the raw signals from components
mfcc = librosa.feature.mfcc(y=y, sr=sr, hop_length=hop, n_mfcc=13)

# first-order differences (delta features)
mfcc_delta = librosa.feature.delta(mfcc)

# Stack and synchronize between beat events
beat_mfcc_delta = librosa.display.util.sync(np.vstack([mfcc, mfcc_delta]),beat_frames)

# Compute chroma features from the harmonic signal
chromagram = librosa.feature.chroma_cqt(y=harmonic,
                                        sr=sr)

# Aggregate chroma features between beat events . use median value of each feature between beat frames
beat_chroma = librosa.display.util.sync(chromagram,
                                        beat_frames,
                                        aggregate=np.median)

# stack all beat-synchronous features together
beat_features = np.vstack([beat_chroma, beat_mfcc_delta])

# saving as .mfcc files

#saving numpy.nd in output.mfcc


# remember to extract only [1st , middle , last]
# now i have rows= 38 , column = dependencies on duration

transpose = beat_features.transpose()

output = 'test.mfcc'
data = np.vstack([transpose[1], transpose[len(transpose) // 2], transpose[len(transpose) - 2]])
data = np.transpose(data)
np.savetxt(output, data)