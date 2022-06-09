import pyinputplus as pyip

bread_type = pyip.inputMenu(['wheat', 'white', 'sourdough', 'rye'], numbered=True)
protein_type = pyip.inputMenu(['chicken', 'turkey', 'ham', 'tofu'], numbered=True)
want_cheese = pyip.inputYesNo('Do you want cheese?')
if want_cheese:
    cheese_type = pyip.inputMenu(['cheddar', 'swiss', 'mozzarella'], numbered=True)
want_mayo = pyip.inputYesNo('Do you want mayo?')
want_mustard = pyip.inputYesNo('Do you want mustard?')
want_lettuce = pyip.inputYesNo('Do you want lettuce?')
want_tomato = pyip.inputYesNo('Do you want tomato?')
number_of_sandwiches = pyip.inputInt(prompt='How many sandwiches do you want?', min=1)
