import re


# create a regex object
phone_regex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phone_regex.search('My number is 415-555-4242.')

# groups() and group(index) method returns a tuple of all the matches
print(mo.groups())
print(mo.string)
print(mo.span())

# pipe |
hero_regex = re.compile(r'Batman|Tina Fey')
mo1 = hero_regex.search('Batman and Tina Fey.')
print(type(mo1))
print(mo1.group())
mo2 = hero_regex.findall('Batman and Tina Fey.')    # findall() returns a list
print(type(mo2))


bat_regex = re.compile(r'Bat(man|mobile|copter|bat)')
mo = bat_regex.search('Batmobile lost a wheel')
print(mo.group())   # mo.group returns the full matched text
print(mo.group(1))  # mo.group returns just the part of the matched text inside the first parentheses group

# Optional matching a group
bat_regex = re.compile(r'Bat(wo)?man')
mo = bat_regex.search("The adventure of Batman")
print(mo.group())
mo = bat_regex.search("The adventure of Batwoman")
print(mo.group())

# Looking for phone number that has an optional area code
phone_regex = re.compile(r'(\d\d\d-)?\d\d\d-\d\d\d\d')
mo = phone_regex.search('My number is 415-555-4242.')
print(mo.group())
mo = phone_regex.search('My number is 555-4242.')
print(mo.group())


greedy_ha_regex = re.compile(r'(Ha){3,5}')
non_greedy_ha_regex = re.compile(r'(Ha){3,5}?')
mo = greedy_ha_regex.search('HaHaHaHaHa')
print(mo.group())
mo = non_greedy_ha_regex.search('HaHaHaHaHa')
print(mo.group())

xmas_regex = re.compile(r'\d+\s\w+')
mo = xmas_regex.findall('12 drummers, 11 pipers, 10 lords, 9 ladies, 8 maids, 7 swans, 6 geese, 5 rings, 4 birds, 3 hens, 2 doves, 1 partridge')
print(mo)

# Making your own character classes
vowel_regex = re.compile(r'[aeiouAEIOU.]')  # no need to escape the dot
mo = vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

# Making a negative character class
non_vowel_regex = re.compile(r'[^aeiouAEIOU.]')
mo = non_vowel_regex.findall('RoboCop eats baby food. BABY FOOD.')
print(mo)

name_regex = re.compile(r'First Name: (.*) Last Name: (.*)')
mo = name_regex.search('First Name: Al Last Name: Sweigart')
print(mo.groups())
