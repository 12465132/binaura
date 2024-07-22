import numpy as np
import onnxruntime as rt
from scipy.io.wavfile import write
from scipy.io.wavfile import read
from pydub import AudioSegment


# Convert mp3 file to wav
audio = AudioSegment.from_mp3('Ignorance is Bliss.mp3')
audio.export('input.wav', format='wav')

# Load the ONNX model
sess = rt.InferenceSession('UVR-MDX-NET-Inst_HQ_3.onnx')

# Load wav file
fs, data = read('input.wav')

#i16 to f32
# data = np.array(data,dtype='f32')
    
# end default constructor
# Make sure the audio data is a 2D numpy array with shape (1, n)
if len(data.shape) == 1:
    data = np.expand_dims(data, 0)

# Run the model
output1, output2 = sess.run(None, {'input': data.astype('float32')})

# Write the output audio files
write('output1.wav', fs, output1[0])
write('output2.wav', fs, output2[0])

# Convert wav files to mp3
output1_audio = AudioSegment.from_wav('output1.wav')
output1_audio.export('output1.mp3', format='mp3')

output2_audio = AudioSegment.from_wav('output2.wav')
output2_audio.export('output2.mp3', format='mp3')