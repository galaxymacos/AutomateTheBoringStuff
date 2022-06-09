import re

import pyinputplus as pyip

# Traditional input
# while True:
#     try:
#         age = int(input("Enter your age: "))
#         if age <= 0:
#             raise ValueError
#         break
#     except ValueError:
#         print("Please enter a valid number")
# print("You are " + str(age) + " years old")

# help(pyip.inputInt)
# # response = pyip.inputNum(prompt="Enter a number: ", min=0, max=100)
# pyip.inputNum(prompt="Enter a number: ", blank=True, timeout=10, limit=5, default='N/A')
#
# # Use regex
# response = pyip.inputStr(allowRegexes=[r'(I|V|X|L|C|D|M)+', r'zero'], prompt="Enter a Roman numeral: ")
# response = pyip.inputStr(blockRegexes=[r'[02468]$'])
#
# # allowRegex override blockRegex
# # even number is still accepted
# response = pyip.inputStr(allowRegexes=[r'[02468]$'], blockRegexes=[r'[02468]$'])


# def adds_up_to_ten(numbers):    # the function parameter is a string
#     sum_num = 0
#     numbers_list = list(numbers)
#     for num in numbers_list:
#         sum_num += int(num)
#     if sum_num == 10:
#         return True
#     raise Exception("The numbers do not add up to 10")  # raise an exception for the pypi to loop
#

# response = pyip.inputCustom(adds_up_to_ten)

while True:
    try:
        response = pyip.inputStr(prompt="Want to know how to keep an idiot busy for hours?")
        yes_regex = re.search(r'(y|Y|([Yy][Ee][Ss]))', response)
        no_regex = re.search(r'(N|n|[Nn][Oo])', response)
        if yes_regex is not None:
            continue
        if no_regex is not None:
            break
        raise Exception(response + " is not a valid response")
    except Exception as e:
        print(response+" is not a valid response.")

while True:
    prompt = 'Want to know how to keep an idiot busy for hours?'
    response = pyip.inputYesNo(prompt, default=True)
    if response == 'no':
        break
