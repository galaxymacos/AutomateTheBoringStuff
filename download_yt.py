from pathlib import Path

import pytube

storage_path = str(Path.cwd())
print(storage_path)
url = input("Enter video url")

pytube.YouTube(url).streams.get_highest_resolution().download(storage_path)
