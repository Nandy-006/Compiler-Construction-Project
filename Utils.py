import os

# Checks if the file has .lwj extension
def checkFile(filepath):
    if os.path.isfile(filepath) and os.path.splitext(os.path.basename(filepath))[1] == ".lwj":
        return None
    else:
        raise Exception("Not a Langwej file")