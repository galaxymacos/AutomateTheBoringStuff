import re

import pyperclip

original_text = str(pyperclip.paste())
regex_phone = re.compile(r'''(
    (\d{3}|\(\d{3}\))?                # area code
    (\s|-|\.)?                        # separator
    (\d{3})                           # first 3 digits
    (\s|-|\.)                         # separator
    (\d{4})                           # last 4 digits
    (\s*(ext|x|ext.)\s*(\d{2,5}))?    # extension
)''', re.VERBOSE)

matches = []
# Create a regex for email addresses
regex_email = re.compile(r'''(
    [a-zA-Z\d._%+-]+      # username
    @                      # @ symbol
    [a-zA-Z\d.-]+         # domain name
    (\.[a-zA-Z]{2,4})      # dot-something
)''', re.VERBOSE)
phone_list = regex_phone.findall(original_text)
for phone in phone_list:
    phone_number = '-'.join([phone[1], phone[3], phone[5]])
    if phone[8] != '':
        phone_number += ' x' + phone[8]
    matches.append(phone_number)

email_list = regex_email.findall(original_text)
for email in email_list:
    matches.append(email[0])
pyperclip.copy('\n'.join(matches))

# 800-420-7240 x1234
# 415-863-9900
# 415-863-9950
# info@nostarch.com
# media@nostarch.com
# academic@nostarch.com
# info@nostarch.com

word_num_regex = re.compile(r',\s\w+')
print(word_num_regex.sub(', X', '12 drummers, 11 pipers, five rings, 3 hens'))
num_regex = re.compile(r'(^\w+)|\d+')
print(num_regex.sub('X', '12 drummers, 11 pipers, five rings, 3 hens'))

three_digit_regex = re.compile(r'^(\d{1,3})(,\d{3})*$')
print(three_digit_regex.search('1234'))

watanabe_regex = re.compile(r'([A-Z]\w*)\sWatanabe')
print(watanabe_regex.search('Xun Watanabe').group())

three_words_regex = re.compile(r'''(
(Alice|Bob|Carol)\s(eats|pets|throws)\s(apples|cats|baseballs).$)''', re.VERBOSE | re.IGNORECASE)
print(three_words_regex.search('Alice throws apples.').group())

date_regex = re.compile(r'''(
    ^(0[1-9]|1[012])
    -
    ([12]\d|3[01])
    -
    \d{4}$
)''', re.VERBOSE)
print(date_regex.search('12-31-1999').group())

# Regex look ahead assertion
# A(?=B) matches A only if it is followed by B
# A(?!B) matches A only if it is not followed by B
# (?<=B)A matches A only if it is preceded by B
# (?<!B)A matches A only if it is not preceded by B
strong_password_regex = re.compile(r'''(
    ^
    (?=.*[A-Z])
    (?=.*[a-z])
    (?=.*\d)
    (?!.*\s)
    .{8,}
    $
)''', re.VERBOSE)
print(strong_password_regex.search('unatAanasr@be1').group())

strip_regex = re.compile(r'^\s*(\S+\s*\S*)\s*$')
print(strip_regex.search(' hello world ').group(1))
# print(strip_regex.sub(, ' hello world '))
# print(strip_regex.sub(strip_regex.search(' hello world ')[1], ' hello world '))