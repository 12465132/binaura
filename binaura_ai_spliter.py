from audio_separator.separator import Separator
import os

try:
    os.mkdir("AiAudio")
except OSError as error:
    print("AiAudio already created")   
try:
    os.mkdir("raw")
except OSError as error:
    print("raw already created")    
try:
    os.mkdir("Instrumental")
except OSError as error:
    print("Instrumental already created")  
try:
    os.mkdir("Vocals")
except OSError as error:
    print("Vocals already created") 
try: 
    os.mkdir("completed_raw")
except OSError as error:
    print("completed_raw already created")  
# Initialize the Separator class (with optional configuration properties, below)
separator = Separator(output_dir="AiAudio")
# Load a machine learning model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
separator.load_model(model_filename='UVR-MDX-NET-Inst_HQ_3.onnx')
# Perform the separation on specific audio files without reloading the model
cleanup_condition1 = input("should completed SPLIT files be moved out of AiAudio to Instrumental and Vocals directory?(y/n) ")
cleanup_condition2 = input(  "should original RAW files be moved out of raw to completed/raw directory?(y/n) ")
for posable_file in os.listdir("raw/"):
    file_stem = posable_file.rsplit(".", maxsplit=1)[0]
    aiaudiofile = file_stem+"_(Instrumental)_UVR-MDX-NET-Inst_HQ_3.wav"
    if aiaudiofile in os.listdir("AiAudio/"):
        continue  
    if not posable_file.endswith((".mp3",".wav",".ogg",".pcm",".aac",".",".")) :
        continue
    output_files = separator.separate("raw/"+posable_file)
    if cleanup_condition1 == "y":
        os.rename("AiAudio/"+file_stem+"_(Instrumental)_UVR-MDX-NET-Inst_HQ_3.wav","Instrumental/"+file_stem+"_(Instrumental).wav")
        os.rename("AiAudio/"+file_stem+      "_(Vocals)_UVR-MDX-NET-Inst_HQ_3.wav",      "Vocals/"+file_stem+      "_(Vocals).wav")
    if cleanup_condition2 == "y":
        os.rename("raw/"+posable_file,"completed/raw/"+posable_file)
print("Separation complete!")