# record here
# automate this to record test data

import os
import pyaudio
import wave
import array
import numpy
import time

CHUNK = 1225
FORMAT = pyaudio.paInt16
CHANNELS = 2
RATE = 44100
RECORD_SECONDS = 40


threshold = 200

data=['divya','prafful','ahaan','nishchith','pravar']
versions = 10
#no of versions = 5

init = data[0]
#enter dirs
for i in range(versions):
    for j in range(5):
        os.system('say Say'+ str(i))
        p = pyaudio.PyAudio()
        WAVE_OUTPUT_FILENAME = 'train/'+init+'/'+ str(i)+'_'+ str(j)+ '.wav'
        time.sleep(0.2)
        stream = p.open(format=FORMAT,
                        channels=CHANNELS,
                        rate=RATE,
                        input=True,
                        frames_per_buffer=CHUNK)

        print("* recording")
        frames = []

        num_sil_frames = 0

        # The device will record for 20 seconds until there has been 0.5
        # second of audio (18 frames) where the energy is less than the threshold

        for _ in range(0, int(RATE / CHUNK * RECORD_SECONDS)):
            data = stream.read(CHUNK)
            frames.append(data)
            nums = array.array('h', data)
            left = numpy.array(nums[1::2])
            energy = 10 * numpy.log(numpy.sum(numpy.power(left, 2)))
            # print(energy)

            if (energy < threshold):
                num_sil_frames = num_sil_frames + 1
            else:
                num_sil_frames = 0

            if num_sil_frames >= 37:
                break

        os.system('say Recording done')
        print("* done recording")

        stream.stop_stream()
        stream.close()
        p.terminate()

        wf = wave.open(WAVE_OUTPUT_FILENAME, 'wb')
        wf.setnchannels(CHANNELS)
        wf.setsampwidth(p.get_sample_size(FORMAT))
        wf.setframerate(RATE)
        wf.writeframes(b''.join(frames))
        wf.close()
        time.sleep(3)