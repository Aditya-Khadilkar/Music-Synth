import subprocess
import os
import glob



def convert2abc(song):
    title = song[9:-4]
    a = subprocess.check_output(['java', '-jar', 'MidiZyx2abc_6.04.jar',song,'-stdout'])
    f = open('input/song.txt', 'w')
    f.write(a.decode('ascii'))
    f.close()
    x = open('input/'+title+'.txt', 'w')
    with open('input/song.txt','r+') as file:
        for line in file:
            if not line.startswith("\n"):
                x.write(line)
    os.remove('input/song.txt')
    n = 2
    nfirstlines = []

    with open('input/'+title+'.txt') as f, open("bigfiletmp.txt", "w") as out:
        for x in range(n):
            nfirstlines.append(next(f))
        for line in f:
            out.write(line)

    # NB : it seems that `os.rename()` complains on some systems
    # if the destination file already exists.
    os.remove('input/'+title+'.txt')
    os.rename("bigfiletmp.txt", 'input/'+title+'.txt')

if __name__ == '__main__':
    midis = glob.glob('rawmidis/*')
    for song in midis:
        convert2abc(song)
