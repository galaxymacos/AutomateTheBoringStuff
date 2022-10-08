import shelve
shelfFile = shelve.open('mydata')
cats = ['Zophie', 'Pooka', 'Simon']
shelfFile['cat'] = cats

list(shelfFile.keys())

list(shelfFile.values())

shelfFile.close()

