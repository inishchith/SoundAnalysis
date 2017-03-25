
import  sklearn
import timeit
import  matplotlib
import numpy as np
import librosa.display

# dir here
gen = input("Enter genre to test (rap,rock,metal,hiphop,rnb,opera) : ")
if gen in ["hiphop","metal","rnb","opera"]:
    y, sr = librosa.load("train/test"+gen+'.m4a')
else :
    y, sr = librosa.load("train/test" + gen + '.mp3')
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
output =  'test.mfcc'
data = np.vstack([transpose[5], transpose[len(transpose) // 2], transpose[len(transpose) -2]])
data = np.transpose(data)
np.savetxt(output, data)

print("done creating test file ")