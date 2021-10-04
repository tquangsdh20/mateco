<p align="center">
  <h1 align="center">Master Text Converter</h1>
</p>

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

### Work with module TTS

#### Initialatize module and setup language


```python
from mateco import TTS
mod = TTS()
#Setup language
mod.setup_language()
```

    Choose Language: 
    
        1. English UK
        2. English US
        3. Chinese
        4. Janpanese
        5. French
        6. Spanish Mexico
        7. Italian
        8. German
        9. Russian
        10. Dutch
        11. Korean
        12. Arabic
        13. Spanish Spain
    
    Enter your choice:  2
    

#### Setup voice


```python
mod.setup_voice()
```

    Voice Options for English US: 
            1. Joey     - Male
            2. Justin   - Little Boy
            3. Matthew  - Male
            4. Salli    - Female
            5. Joanna   - Female
            6. Ivy      - Little Girl
            
        Enter your choose:  4
    

#### Update the text you want to convert & Save it


```python
mod.update('I try this, try that, try everything.')
mod.play()
mod.save('output/audio.mp3')
```

### Work with module IPA 

#### Initialize module IPA


```python
from mateco import IPA
#Default is English UK
mod = IPA()
```

#### Update text to convert


```python
en_uk = mod.get_ipa('I dropped my food on my foot')
print(en_uk)
```

    aɪ drɒpt maɪ fuːd ɒn maɪ fʊt
    

#### Test with boths


```python
#Setup English UK IPA
mod = IPA(1)
en_uk = mod.get_ipa('potato, tomato')
print('Bristh say:',en_uk)
#Setup English US IPA
mod = IPA(2)
en_us = mod.get_ipa('potato, tomato')
print('America say:',en_us)
```

    Bristh say: pəˈteɪtəʊ, təˈmɑːtəʊ
    America say: pəˈteɪˌtoʊ, təˈmeɪˌtoʊ
    
### Change Log

<b>PLANNING</b>  
Module TTS: Support Text to Pretty Speech with 13 languages.  
Module IPA: Support Text to IPA  
Note: LIMITED Online converter

### URL: https://github.com/tquangsdh20/mateco/
