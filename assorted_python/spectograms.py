import numpy as np
import librosa 
from pydub import AudioSegment
import pyfftw
import threading
#frame size
#hop length = frame increment
librosa.set_fftlib(pyfftw.interfaces.numpy_fft)
sound = AudioSegment.from_file("raw/440Hz_44100Hz_16bit_05sec.wav", channels=1)
l_channel = AudioSegment.from_file("raw/440Hz_44100Hz_16bit_05sec.wav", channels=1)
r_channel = AudioSegment.from_file("raw/440Hz_44100Hz_16bit_05sec.wav", channels=1)
# l_channel,r_channel = sound.split_to_mono()

n_fft = 1024
hop_length = 32
win_length=512
shift = 10
window = 'blackmanharris'

r_nprw = np.frombuffer(r_channel._data, dtype=np.int16).astype(np.float32)
r_stft = librosa.stft(             r_nprw,n_fft=n_fft,hop_length=hop_length,win_length=win_length,window=window,center=True)
r_fd =   librosa.istft(stft_matrix=r_stft,n_fft=n_fft,hop_length=hop_length,win_length=win_length,window=window,center=True)
r_channel_new  = AudioSegment(np.array(r_fd, dtype=np.int16).tobytes(), frame_rate = sound.frame_rate, sample_width=2, channels = 1)
r_dbfs = r_channel_new.dBFS

l_nprw = np.frombuffer(l_channel._data, dtype=np.int16).astype(np.float32)
l_stft = librosa.stft(             l_nprw,n_fft=n_fft,hop_length=hop_length,win_length=win_length,window=window,center=True)
(y_l,x_l) = l_stft.shape
print(l_stft.shape)
l_stft = np.ascontiguousarray(np.flip(l_stft, axis=0))
print(l_stft.shape)
l_stft.resize((y_l+shift, x_l))
print(l_stft.shape)
l_stft = l_stft[shift:y_l+shift,:]
print(l_stft.shape)
l_stft = np.ascontiguousarray(np.flip(l_stft, axis=0))
# l_stft.resize((y_l+shift,x_l))
# l_stft = l_stft[shift:y_l+shift,:]
l_fd =   librosa.istft(stft_matrix=l_stft,n_fft=n_fft,hop_length=hop_length,win_length=win_length,window=window,center=True)
l_channel_new  = AudioSegment(np.array(l_fd, dtype=np.int16).tobytes(), frame_rate = sound.frame_rate, sample_width=2, channels = 1)
# l_channel_new.overlay(l_channel)
l_dbfs = l_channel_new.dBFS
delta_dbfs = r_dbfs - l_dbfs
# l_channel_new = l_channel_new.aply_gain(delta_dbfs)

sound_new = AudioSegment.from_mono_audiosegments(l_channel_new, r_channel_new)
sound_new.export("assorted/440Hz_44100Hz_16bit_05sec.wav", bitrate="320k")
print(l_stft.shape)
print(l_stft.ndim)
print(l_stft.dtype)
# import matplotlib.pyplot as plt
# fig, ax = plt.subplots()
# img = librosa.display.specshow(librosa.amplitude_to_db(np.abs(l_stft),
#                                                        ref=np.max),
#                                y_axis='fft', x_axis='s', ax=ax,n_fft=n_fft,hop_length=hop_length,win_length=win_length,)
# ax.set_title('Power spectrogram')
# fig.colorbar(img, ax=ax, format="%+2.0f dB")
# plt.savefig('graph.png', format='png')
