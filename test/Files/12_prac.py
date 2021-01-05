# to rename a file

import os
oldname = "tochangename.txt"
newname = "renamed_by_python.txt"

with open(oldname) as f:
    content = f.read()

with open(newname, 'w') as f:
    f.write(content)

os.remove(oldname)


# to rename a folder