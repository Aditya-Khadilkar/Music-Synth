import os
import glob

def delete_files():
    files = glob.glob('tempfilesm/*')
    for f in files:
        os.remove(f)

    files = glob.glob('input/*')
    for f in files:
        os.remove(f)

    files = glob.glob('output/*')
    for f in files:
        os.remove(f)

    files = glob.glob('rawmidis/*')
    for f in files:
        os.remove(f)

if __name__ == '__main__':
    delete_files()