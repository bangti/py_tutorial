import os
import shutil

path = "test36.txt"
# path = "empty_folder"

try:
    os.remove(path) # delete a file
    # os.rmdir(path) # delete a folder
    # shutil.rmtree(path) # delete a folder & file
except FileNotFoundError:
    print("That file was not found")
except PermissionError:
    print("You do not have permission to delete that")
except OSError:
    print("You cannot delete that using that function")
else:
    print(path+" was deleted")


