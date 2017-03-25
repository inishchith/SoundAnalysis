
import  sklearn
import timeit
import  matplotlib
import numpy as np
import librosa.display

# dir here
print("Detect animal ")
an= input("Select animal for testing (dog,cat,lion): ")
nu = int(input("Enter any number less than or equal to 10"))
y, sr = librosa.load("train/"+an+"/sound"+str(10)+".wav")

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
data = np.vstack([transpose[1], transpose[len(transpose) // 2], transpose[len(transpose) - 2]])
data = np.transpose(data)
np.savetxt(output, data)

print("done")