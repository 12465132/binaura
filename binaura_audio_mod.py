from pydub import AudioSegment
import librosa 
import numpy as np 
import os

def pitch_shift(sound,n_steps):
    y = np.frombuffer(sound._data, dtype=np.int16).astype(np.float32)
    y = librosa.effects.pitch_shift(y=y, sr=sound.frame_rate, n_steps=n_steps)
    a  = AudioSegment(np.array(y , dtype=np.int16).tobytes(), frame_rate = sound.frame_rate, sample_width=2, channels = 1)
    return a


try:
    os.mkdir("Instrumental")
except OSError as error:
    print("Instrumental already created")   
try:
    os.mkdir("Vocals")
except OSError as error:
    print("Vocals already created")   
try:
    os.mkdir("completed/Instrumental")
except OSError as error:
    print("completed/Instrumental already created")   
try:
    os.mkdir("completed/Vocals")
except OSError as error:
    print("completed/Vocals already created")   
try:
    os.mkdir("final")
except OSError as error:
    print("final already created")   
cleanup_condition1 = input("should original SPLIT files be moved out of Instrumental and Vocals to completed/Vocals and completed/Instrumental directory?(y/n) ")
half_steps = input("how many halfsteps should all audio be shifted by? ")
for posable_file in os.listdir("Instrumental/"):
    if posable_file.endswith((".mp3",".wav",".ogg",".pcm",".aac",".",".")) :
        file_stem = posable_file.rsplit("_(Instrumental)", maxsplit=1)[0]
        file_type = posable_file.rsplit("_(Instrumental)", maxsplit=1)[1]
        vocal_file_path_reconstruct = file_stem + "_(Vocals)" + file_type
        file_instrumental = os.path.join("Instrumental/", posable_file)
        file_vocal =        os.path.join(       "Vocals/", vocal_file_path_reconstruct)
        left_channel,right_channel = AudioSegment.from_file(file_instrumental).split_to_mono()
        left_channel    = pitch_shift(left_channel ,half_steps)
        right_channel   = pitch_shift(right_channel,half_steps)
        stereo_sound_shifted = AudioSegment.from_mono_audiosegments(left_channel, right_channel)
        stereo_sound_Instrumental = AudioSegment.from_file(file_instrumental)
        stereo_sound_Vocals = AudioSegment.from_file(file_vocal)
        stereo_sound_shifted = stereo_sound_shifted.overlay(stereo_sound_Instrumental)
        stereo_sound_shifted = stereo_sound_shifted.overlay(stereo_sound_Vocals)
        stereo_sound_shifted.export("final/"+file_stem + "_" + half_steps +".wav")
        print("file : " + "final/" + file_stem + half_steps +".wav" + " completed")
        if cleanup_condition1 == "y":
            os.rename("Instrumental/"+file_stem+"_(Instrumental)"+file_type,"completed/Instrumental/"+file_stem+"_(Instrumental).wav")
            os.rename(      "Vocals/"+file_stem+      "_(Vocals)"+file_type,      "completed/Vocals/"+file_stem+      "_(Vocals).wav")
