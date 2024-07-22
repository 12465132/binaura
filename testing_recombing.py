from pydub import AudioSegment
import librosa 
import numpy as np 

def pitch_shift(sound,n_steps):
    y = np.frombuffer(sound._data, dtype=np.int16).astype(np.float32)
    y = librosa.effects.pitch_shift(y=y, sr=sound.frame_rate, n_steps=n_steps)
    a  = AudioSegment(np.array(y , dtype=np.int16).tobytes(), frame_rate = sound.frame_rate, sample_width=2, channels = 1)
    return a

left_channel,right_channel = AudioSegment.from_file("1_Ignorance is Bliss_(Instrumental).mp3").split_to_mono()
left_channel    = pitch_shift(left_channel ,1)
right_channel   = pitch_shift(right_channel,1)

stereo_sound_shifted = AudioSegment.from_mono_audiosegments(left_channel, right_channel)
stereo_sound_Instrumental = AudioSegment.from_file("1_Ignorance is Bliss_(Instrumental).mp3")
stereo_sound_Vocals = AudioSegment.from_file("1_Ignorance is Bliss_(Vocals).mp3")
stereo_sound_shifted.overlay(stereo_sound_Instrumental)
# stereo_sound_shifted.overlay(stereo_sound_Vocals)
stereo_sound_shifted.export("shift_Ignorance is Bliss.wav")
# sound1 = AudioSegment.from_file("1_Ignorance is Bliss_(Instrumental).mp3")
# sound2 = AudioSegment.from_file("1_Ignorance is Bliss_(Vocals).mp3")

# played_togther = sound1.overlay(sound2)

# file_handle = played_togther.export("1_Ignorance is Bliss.mp3",
#                            format="mp3",
#                            bitrate="192k")
# Load an audio file
# audio = AudioSegment.from_file("Ignorance is Bliss.mp3")
# Laudio, Raudio = audio.split_to_mono()
# Laudio=pitch_shift(Laudio,1.5)
# pitch_shift(Raudio,1.5)
# Laudio.export("l_Ignorance is Bliss.wav")
# Concatenate the chunks back together
# shifted_audio = pitch_shift(audio, 1)
# araw_data   = audio.raw_data
# aframe_rate = audio.frame_rate
# achannels   = audio.channels
# # print("", araw_data)
# print(aframe_rate)
# print(achannels)

# audio.export("1_Ignorance is Bliss.wav")
