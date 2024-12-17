import keyword

slowa = ["for", "print", "break", "done", "bad"]
for slowo in slowa:
    print(f"{slowo}: {'jest' if keyword.iskeyword(slowo) else 'nie jest'} słowem kluczowym")
