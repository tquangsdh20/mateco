<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/mateco/main/.github/header.svg">
</p>

<p align="center"><img src="https://github.com/tquangsdh20/mateco/actions/workflows/test.yml/badge.svg"> <a href="https://codecov.io/github/tquangsdh20/mateco/commit/813bae77e548561e373c9a882199e795c44592a7"><img src="https://codecov.io/gh/tquangsdh20/mateco/branch/main/graphs/badge.svg?branch=main"></a> <img src = "https://img.shields.io/pypi/pyversions/mateco"></p>

## Features

- Support text to speech with many pretty voices options
- Support download file mp3 from TTS
- Support convert text to IPA (International Phonetic Alphabet) with English UK and English US

## Installation
**Windows**
```
python -m pip install mateco
```
**Linux**
```
pip install mateco
```
**macOS**
```
sudo pip3 install mateco
```
## How does it work?

### Working with module TTS

#### Setup Language for Converting

To setup language and voice using the method `setup_voice(language_code)`, where `language_code` :

- English US : `am`
- English UK : `br`
- Portuguese (Brazil): `pt-br`
- Portuguese (Portugal): `pt`
- The other languages : `ISO LANGUAGE CODE 639-1`

```python
from mateco import TTS

# Initialization for Module TTS
mod = TTS()

# Choice the voice for America English
mod.setup_voice('am')

# Convert to audio data
mod.convert('Welcome to Master Text Converter library. I hope it\'s useful for you.')
mod.speak()
mod.save_to_file('audio.mp3')

# Change the language
mod.setup_voice('fr')
mod.convert('Je parle un peu français')
mod.speak()
mod.save_to_file('audio_french.mp3')
mod.close()
```

Output

```
>> All voices for your language:
>>    1. Joey - Male - SAPI5
>>    2. Justin - Male - SAPI5
>>    3. Matthew - Male - SAPI5
>>    4. Salli - Female - SAPI5
>>    5. Joanna - Female - SAPI5
>>    6. Ivy - Female - SAPI5
>> Make your choice: 3
```

### Work with module IPA 

#### Initialize module IPA


```python
from mateco import IPA

# Setup English UK IPA
mod = IPA('am')
en_uk = mod.get_ipa('potato, tomato')
print('Bristh say:',en_uk)

# Setup English US IPA
mod = IPA('br')
en_us = mod.get_ipa('potato, tomato')
print('America say:',en_us)

# Working with Bulk - List of the texts
bulk = ['potato', 'tomato', 'schedule']
results = mod.get_ipas(bulk)
print(results)
```

Output

```
>> Bristh say: pəˈteɪˌtoʊ, təˈmeɪˌtoʊ
>> America say: pəˈteɪtəʊ, təˈmɑːtəʊ
>> ['pəˈteɪtəʊ', 'təˈmɑːtəʊ', 'ˈʃɛdjuːl']
```

<p align="center">
  <img src="https://raw.githubusercontent.com/tquangsdh20/mateco/main/.github/footer.svg">
</p>

<a href="https://github.com/tquangsdh20/mateco"><p align="center"><img src="https://img.shields.io/badge/Github-tquangsdh20-orange?style=social&logo=github"></p></a>