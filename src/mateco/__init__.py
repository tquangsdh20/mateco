"""Text to Pretty Speech library"""
from .ipa import _IPA
from .tts import _TTS
import os
import sys

class TTS(_TTS):
    '''Guideline:\n
    - Call `setup_language()` to choose language.\n
    - Call `setup_voice()` in order to choose voice.\n
    - Call `update( <text here> )` for converting text to speech.\n
    - Call `play()` for checking the sound.\n
    - Eventually, `save(<filename>)` for getting the file.
    ~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~
    Parameters:\n
    - `language_id` call method `language_opts()` to get language_id\n
    - `proxy` using proxy to connect the server'''
    def setup_language(self)-> None:
        self._setup_language()

    def setup_voice(self)-> None:
        self._setup_voice()

    def update(self,text:str) -> None:
        self._update(text)
    
    def play(self) -> None:
        try:
            self._play()
        except:
            print('This method is not support for your operating system. Please save local and play it manually.')

    def save(self,filename:str)->None:
        self._save(filename)

class IPA(_IPA):
    '''Parameter:\n
    - `language_id` (optional) : Choose English UK (1) or English US (2). Default is English UK.
    ~~~~~~~~~~~~~~~~~~~~
    Method:\n
    - `get_ipa(text,proxy)` return the IPA of the English content, `proxy` paramater is optional
    ~~~~~~~~~~~~~~~~~~~~
    Note: About 100 requests for getting IPA server will give you a Error message "many requests", \n
    in this case using proxy could deal with it.
    '''

    def get_ipa(self,text:str,proxy=None) -> str:
        '''`text` is the content convert to IPA'''
        return self._get_ipa(text,proxy)