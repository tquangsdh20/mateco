from mateco import TTS
#Setup with Language ID = 2 (English US)
mod = TTS(2)
#Setup language
#mod.setup_language()
print('This example is setup with Language English US.')
mod.setup_voice()
mod.update('Welcome to Master Text Converter library. I hope it\'s useful for you.')
mod.play()
#mod.save('/output/audio.mp3')