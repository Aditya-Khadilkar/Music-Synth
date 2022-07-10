from functions.preprocess1 import *
from functions.preprocess2 import *
from functions.prepboilerplate import *
import os
def activateRed(songtitle):
    #arr = os.listdir('input')
    filename = 'input/'+ songtitle
    activateBoilerplate(filename)
    ls = seperator('tempfilesm/verse2.txt')#change to 1
    word2tok, tok2word, toksong = dictGenerator(ls)
    with open('tempfilesm/word2tok.json', 'w') as fp:
        json.dump(word2tok, fp)
    with open('tempfilesm/tok2word.json', 'w') as fp:
        json.dump(tok2word, fp)
    with open('tempfilesm/toksong.json', 'w') as fp:
        json.dump(toksong, fp)
    f = open('tempfilesm/toksong.json',) 
    data = json.load(f)
    tdata = data
    iterNumber = -1
    mem ={}
    tData, iterNumber, mem = bpe(tdata, iterNumber, mem)
    keys, valist = makeValistandKeys(mem)
    valist = expansionLoop(valist)
    finaldict = dict(zip(keys, valist)) 
    with open("tempfilesm/BPEdict.json", "w") as outfile:  
        json.dump(finaldict, outfile)
    with open("tempfilesm/BPEtoksong.json", "w") as outfile:  
        json.dump(tData, outfile)
if __name__=="__main__":

    activateRed('FakeLove.txt')
    '''
    arr = os.listdir('input')
    filename = 'input/'+ str(arr[0])
    activateBoilerplate(filename)
    ls = seperator('tempfiles/verse1.txt')
    word2tok, tok2word, toksong = dictGenerator(ls)
    with open('tempfiles/word2tok.json', 'w') as fp:
        json.dump(word2tok, fp)
    with open('tempfiles/tok2word.json', 'w') as fp:
        json.dump(tok2word, fp)
    with open('tempfiles/toksong.json', 'w') as fp:
        json.dump(toksong, fp)
    f = open('tempfiles/toksong.json',) 
    data = json.load(f)
    tdata = data
    iterNumber = -1
    mem ={}
    tData, iterNumber, mem = bpe(tdata, iterNumber, mem)
    keys, valist = makeValistandKeys(mem)
    valist = expansionLoop(valist)
    finaldict = dict(zip(keys, valist)) 
    with open("tempfiles/BPEdict.json", "w") as outfile:  
        json.dump(finaldict, outfile)
    with open("tempfiles/BPEtoksong.json", "w") as outfile:  
        json.dump(tData, outfile)
    
    '''