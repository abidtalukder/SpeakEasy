import pyaudio
import wave

# initialize the pyaudio object
p = pyaudio.PyAudio()

# open the microphone stream
stream = p.open(format=pyaudio.paInt16, channels=1, rate=44100, input=True, frames_per_buffer=1024)

# start recording
frames = []
while True:
    # read the audio data
    data = stream.read(1024)
    # add the data to the frames list
    frames.append(data)
    print(len(frames))
    # check if the user has stopped speaking
    if len(frames) > 1000:
        break

# stop recording
stream.stop_stream()
stream.close()

