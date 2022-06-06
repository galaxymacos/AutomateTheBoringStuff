import sys

import pyperclip as pyperclip

text = {'agree': """Yes, I agree. That sounds fine to me.""",
        'busy': """Sorry, can we do this later this week or next week?""",
        'upsell': """Would you consider making this a monthly donation?"""}

if len(sys.argv) < 2:
    print('Usage: ./mclip.py [key_phrase] - copy phrase text')
    sys.exit()

key_phrase = sys.argv[1]

if key_phrase in text:
    pyperclip.copy(text[key_phrase])
    print("Copied text for " + key_phrase)

print(pyperclip.paste())
