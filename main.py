from tkinter.filedialog import askdirectory
from pathlib import Path

import os
import shutil

downloads = str(Path.home() / "Downloads")
downloads = r'{}'.format(downloads)

# Open Folder, Fail Safe for Special Characters
organize = askdirectory(title='Select Folder to Organize', initialdir=downloads, mustexist=True)
organize = r'{}'.format(organize)

ext = {item.split('.')[-1] for item in os.listdir(organize) if os.path.isfile(os.path.join(organize, item))}

# Create folders
for exten in ext:

    if not os.path.exists(os.path.join(organize, exten)):
        os.makedirs(os.path.join(organize, exten))

# Move Files
for item in os.listdir(organize):
    if os.path.isfile(os.path.join(organize, item)):
        filee = item.split(".")[-1]
        shutil.move(os.path.join(organize, item), os.path.join(organize, filee, item))

