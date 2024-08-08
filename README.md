requires python3 pip numpy librosa audio_separator pydub installed 
once you have python3 and pip installed and on the path you can do:
pip install numpy pydub librosa audio_separator
binaura_ai_spliter.py expects raw audio files in the raw folder
binaura_audio_mod.py expects split Vocals and Instrumental audio files to be in those folders respectively and of the same name except with _(Vocals) or _(Instrumental) added to the end of the file stem
for example, Instrumental/test_(Instrumental).wav and Vocals/test_(Vocals).wav 
final files are denoted with the number of half notes they have been shifted for binaural effect
assorted files are not of any use or purpose