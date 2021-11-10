import subprocess
import os
import glob


def makemid():
    files = glob.glob('output/*')
    for f in files:
        title = f[7:-4]
        title = 'generatedMIDIs/'+title+'.mid'
        #print(title)
        subprocess.run(['abc2midi', f, '-o',title])

if __name__ == '__main__':
    makemid()