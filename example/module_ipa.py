from mateco import IPA


# Setup English UK IPA
mod = IPA("br")
en_uk = mod.get_ipa("potato, tomato")
print("Bristh say:", en_uk)


# Setup English US IPA
mod = IPA("am")
en_us = mod.get_ipa("Master Text Converter")
print("America say:", en_us)


# Working with Bulk - List of the texts
bulk = ["potato", "tomato", "schedule"]
results = mod.get_ipas(bulk)
print(results)
