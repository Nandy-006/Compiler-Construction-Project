import os

def checkFile(filepath):
    print("filepath:",filepath)
    if os.path.isfile(filepath) and os.path.splitext(os.path.basename(filepath))[1] == ".lwj":
        return None
    else:
        raise Exception("Not a Langwej file")