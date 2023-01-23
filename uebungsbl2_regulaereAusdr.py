import re


def groesse_regex (word):
     pattern = re.compile(r"[1]{0,1}[0-9]{0,2} cm| [2]{1}[0]{2} cm")
     match = pattern.match(word)
     if match:
        return match.group()
     return "Ausdruck ist nicht korrekt"

print(groesse_regex("150cm"))
print(groesse_regex("202 cm"))
print(groesse_regex("150 cm"))
print(groesse_regex("199 cm"))

def zwischenbereich(word):
    pattern = re.compile(r"[1]{1}[2]{1}[3-9]{1}|[1]{1}[3-9]{1}[0-9]{1}|[2-4]{1}[0-9]{1}[0-9]{1}|[5]{1}[0-2]{1}[0-9]{1}|[5]{1}[3]{1}[0-6]{1}")
    match = pattern.match(word)
    if match:
        return match.group()
    return "Ausdruck ist nicht korrekt"

print(zwischenbereich("123"))
print(zwischenbereich("122"))
print(zwischenbereich("0"))
print(zwischenbereich("50"))
print(zwischenbereich("537"))
print(zwischenbereich("404"))
print(zwischenbereich("536"))








  