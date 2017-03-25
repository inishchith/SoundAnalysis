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
import timeit
import  matplotlib
import numpy as np
import librosa.display

# Load from dir - .wav file : , init example
# dir = train/cats .mp3 train/dogs .mp3

data = ["rap","rock","hiphop","metal","rnb",'opera']

#version count
start= 1
stop = 5

st = timeit.default_timer()
for name in data:
    for v in range(start,stop):
        #dir her
        if name=='hiphop' or name == 'rnb' or name=='metal':
            y, sr = librosa.load('train/' + name + '/' + name + str(v) + '.m4a')
        else:
            y,sr = librosa.load('train/'+name+'/'+name+str(v)+'.mp3')
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
        #print(transpose)
        output =  "train/"+name+'m/'+ str(v)+'.mfcc'
        data=np.vstack([transpose[4],transpose[len(transpose)//2],transpose[len(transpose)-4]])
        data = np.transpose(data)
        np.savetxt(output, data)
    print("Done with "+ name )

sp=timeit.default_timer()
print("time taken = ",(sp-st))