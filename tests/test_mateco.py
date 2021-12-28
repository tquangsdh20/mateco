from mateco import __version__
from mateco import IPA, TTS

import unittest


def test_version():
    assert __version__ == "1.4.1"


class Test_Module_IPA(unittest.TestCase):
    def test_get_ipa(self):
        # Setup English UK IPA
        bulk = ["potato", "tomato", "schedule"]
        mod = IPA("br")
        en_uk = mod.get_ipa("potato, tomato")
        bulk_uk = mod.get_ipas(bulk)
        bulk = ["potato", "tomato", "schedule"]
        mod = IPA("am")
        en_us = mod.get_ipa("potato, tomato")
        bulk_us = mod.get_ipas(bulk)
        self.assertNotEqual(en_uk, en_us)
        self.assertNotEqual(bulk_uk, bulk_us)


class Test_Module_TTS(unittest.TestCase):
    def test_tts(self):
        mod = TTS()

        # Choice the voice for America English
        mod.setup_voice("am", 2)

        # Convert to audio data
        audio = mod.convert(
            "Welcome to Master Text Converter library. I hope it's useful for you."
        )
        mod.save_to_file("audio.mp3")
        mod.close()
        self.assertIsInstance(audio, bytes)


if __name__ == "__main__":
    unittest.main()
