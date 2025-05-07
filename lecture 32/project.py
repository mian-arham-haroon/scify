import sounddevice
from scipy.io.wavfile import write

def voice(seconds,file):
    print("-----------start recording----------")
    recording=sounddevice.rec((seconds*44100),samplerate=44100,channels=2)
    sounddevice.wait()
    write(file,44100,recording)
    print("Your recording is finished")
voice(30,"rec1.wav")


