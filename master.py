from functions.red import *
from functions.blue import *
from functions.markov import *
from functions.prepboilerplate import*
from functions.preprocess1 import *
from functions.preprocess2 import *
import random
from mid2abc import *
from makemidi import *
from deletedis import *

if __name__ == '__main__':
    midis = glob.glob('rawmidis/*')
    for song in midis:
        convert2abc(song)
    abcs = os.listdir('input')
    for i in abcs:
        try:
            activateRed(i)
            markovLoop(200)
            activateBLUE(i)
        except:
            print("Error: "+i)
    makemid()
    #delete_files()