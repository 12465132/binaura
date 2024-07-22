import numpy as np
import librosa 
from pydub import AudioSegment


#frame size
#hop length = frame increment
sound = AudioSegment.from_file("Living a Lie.mp3")
l_channel,r_channel = sound.split_to_mono()
n_fft = 2**6
hop_length = 2**4
l_stft = librosa.stft(np.frombuffer(l_channel._data, dtype=np.int16).astype(np.float32),n_fft=n_fft,hop_length=hop_length)
r_stft = librosa.stft(np.frombuffer(r_channel._data, dtype=np.int16).astype(np.float32),n_fft=n_fft,hop_length=hop_length)
l_fd = librosa.istft(stft_matrix=l_stft,                                           
            n_fft=1024,hop_length=512,win_length=None,window='hann',center=True)
l_fd = librosa.istft(stft_matrix=l_stft,
            n_fft=1024,hop_length=512,win_length=None,window='hann',center=True)
l_channel_new  = AudioSegment(np.array(l_fd, dtype=np.int16).tobytes(),
                              n_fft=1024,hop_length=512,win_length=None,window='hann',center=True)
r_channel_new  = AudioSegment(np.array(l_fd, dtype=np.int16).tobytes(),
                              n_fft=1024,hop_length=512,win_length=None,window='hann',center=True)
sound_new = AudioSegment.from_mono_audiosegments(l_channel_new, r_channel_new)
sound_new.export("Living a Lie.wav")
print(l_stft.shape)
print(l_stft.ndim)
print(l_stft.dtype)

my_sample_rate = 48000
# step1 - converting a wav file to numpy array and then converting that to mel-spectrogram
my_audio_as_np_array, my_sample_rate = librosa.load("Living a Lie.mp3")

# step2 - converting audio np array to spectrogram
spec = librosa.feature.melspectrogram(y=my_audio_as_np_array,
                                        sr=my_sample_rate,
                                            n_fft=1024,
                                            hop_length=512,
                                            win_length=None,
                                            window='hann',
                                            center=True,
                                            pad_mode='reflect',
                                            power=2.0)
                                            #n_mels=128)

# step3 converting mel-spectrogrma back to wav file

res = librosa.feature.inverse.mel_to_audio(spec,
                                           sr=my_sample_rate,
                                           n_fft=1024,
                                           hop_length=512,
                                           win_length=None,
                                           window='hann',
                                           center=True,
                                           pad_mode='reflect',
                                           power=2.0,
                                           n_iter=32)
                                           #n_mels=128)

# step4 - save it as a wav file
import soundfile as sf
sf.write("test2.wav", res, my_sample_rate)