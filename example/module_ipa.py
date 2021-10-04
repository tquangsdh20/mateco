from mateco import IPA
#Setup English UK IPA
mod = IPA(1)
en_uk = mod.get_ipa('potato, tomato')
print('Bristh say:',en_uk)
#Setup English US IPA
mod = IPA(2)
en_us = mod.get_ipa('potato, tomato')
print('America say:',en_us)