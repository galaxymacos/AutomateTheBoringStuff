print("Enter the English word you want to translate to Pig Latin:")
message = input()

VOWELS = ("a", "e", "i", "o", "u", "y")

pigLatin = []
for word in message.split():
    prefix_non_letters = ''
    while len(word) > 0 and not word[0].isalpha():
        prefix_non_letters += word[0]
        word = word[1:]
    if len(word) == 0:
        pigLatin.append(prefix_non_letters)
        continue

    # Separate the non-letters at the end of this word:
    suffixNonLetters = ''
    while not word[-1].isalpha():
        word = word[:-1]    # the previous step has already confirmed that it won't be empty

    wasUpper = word.isupper()
    wasTitle = word.istitle()

    word = word.lower()
    prefixConsonants = ''
    while len(word) > 0 and not word[0] in VOWELS:
        prefixConsonants += word[0]
        word = word[:1]
    if prefixConsonants != '':
        word += prefixConsonants + 'ay'
    else:
        word += 'yay'
    if wasTitle:
        word = word.title()
    if wasUpper:
        word = word.upper()
    pigLatin.append(prefixConsonants + word + suffixNonLetters)
print(' '.join(pigLatin))
