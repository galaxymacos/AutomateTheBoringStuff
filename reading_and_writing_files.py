import os
import sys
from pathlib import Path
print(str(Path('spam', 'bacon', 'eggs')))

# join file names
my_files = ['accounts.txt', 'details.csv', 'invite.docx']
for my_file in my_files:
    print(Path(r'C:/Users/AL', my_file))

# Use / to join paths
path1 = Path('spam') / 'bacon' / 'eggs'
path2 = Path('spam') / Path('bacon/eggs')
path3 = Path('spam') / Path('bacon', 'eggs')
print(path1, path2, path3)

print(sys.platform)

# the current working directory
print(Path.cwd())
os.chdir('/Users/xunruan')
print(Path.cwd())
print(Path.home())

# make a directory from Path object
path = Path.cwd() / 'new_dir'
print(path)
path.mkdir()
