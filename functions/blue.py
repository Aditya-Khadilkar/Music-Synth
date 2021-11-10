import json



def reverseBPE(BPElist, BPEdict):
    revBPE = []
    for i in BPElist:
        if i<0:
            i = str(i)
            enc = BPEdict[i]
            for j in enc:
                revBPE.append(j)
        else:
            revBPE.append(i)
    return revBPE

#print(rbp)

def tok2wordConv(toklist, tok2word):
    finalABC = ''
    for i in toklist:
        if i==0:
            i = str(i)
            word = tok2word[i]
            finalABC = finalABC + word
            finalABC = finalABC + "\n"
            #add \n
        else:
            i = str(i)
            word = tok2word[i]
            finalABC = finalABC + word
    return finalABC

def makeFile(verses, boilerplate,name):
    final = ''
    for i in boilerplate:
        if i.startswith('<New Voice here>'):
            final = final+verses
        else:
            final = final+i
    f2 = open("output/"+name,"w+")
    f2.write(final)    


def activateBLUE(name):
    f = open('tempfilesm/generated.json') #BPEtoksong
    BPElist = json.load(f)
    f = open('tempfilesm/BPEdict.json') 
    BPEdict = json.load(f)
    f = open('tempfilesm/tok2word.json') 
    tok2word = json.load(f)
    rbp = reverseBPE(BPElist, BPEdict)
    original = tok2wordConv(rbp, tok2word)
    boilerplate = open("tempfilesm/head.txt","r")
    makeFile(original,boilerplate,name)

if __name__ == "__main__":
    activateBLUE('song.txt')
