from audio_separator.separator import Separator



# Initialize the Separator class (with optional configuration properties, below)
separator = Separator()
# Load a machine learning model (if unspecified, defaults to 'model_mel_band_roformer_ep_3005_sdr_11.4360.ckpt')
separator.load_model(model_filename='UVR-MDX-NET-Inst_HQ_3.onnx')
# Perform the separation on specific audio files without reloading the model
output_files = separator.separate('Ignorance is Bliss.mp3')

print(f"Separation complete! Output file(s): {' '.join(output_files)}")