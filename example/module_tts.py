from mateco import TTS

# Initialization for Module TTS
mod = TTS()

# Choice the voice for America English
mod.setup_voice("am")

# Convert to audio data
mod.convert("Welcome to Master Text Converter library. I hope it's useful for you.")
mod.speak()
mod.save_to_file("audio.mp3")

# Change the language
mod.setup_voice("fr")
mod.convert("Je parle un peu français")
mod.speak()
mod.save_to_file("audio_french.mp3")
# Must be closed after done
mod.close()
