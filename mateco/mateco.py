from typing import Any, List
from pyfreetts import Text2Speech
from text2ipa import get_IPA, get_IPAs


class TTS(Text2Speech):
    """Converter from Text to Speech with many pretty voice"""

    ...


class IPA:
    def __init__(self, language):
        self.language = language

    def get_ipa(self, text: str, proxy: Any = None) -> str:
        retval = str()
        retval = get_IPA(text, self.language, proxy)
        return retval

    def get_ipas(self, bulk: List[str], proxy: Any = None) -> List[str]:
        retbulk = list()
        retbulk = get_IPAs(bulk, self.language, proxy)
        return retbulk
