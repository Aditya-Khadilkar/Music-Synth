import json
from collections import Counter 
import itertools


  
def most_frequent(List): 
    occurence_count = Counter(List) 
    return occurence_count.most_common(1)[0] 
    
def replaceTop(A, tup, iterNumber):
    x,y = tup
    #print('before for loop: ', len(A))
    i = 0
    while i < len(A)-1:
        if x== A[i] and y== A[i+1]:
                A[i] = iterNumber
                A.pop(i+1)
        i +=1
    #print('After for loop: ', len(A))
    

def bpe(A, iterNumber, mem):
    tups = []
    for i in range(len(A)-1):
        tup = (A[i],A[i+1])
        tups.append(tup)
    topUnit,freq = most_frequent(tups)
    while freq>1:
        mem[iterNumber] = topUnit
        #print('before call: ', len(A))
        replaceTop(A, topUnit, iterNumber)
        #print('after call: ', len(A))
        iterNumber = iterNumber - 1
        #print(A)
        tups = []
        for i in range(len(A)-1):
            tup = (A[i],A[i+1])
            tups.append(tup)
        topUnit,freq = most_frequent(tups)
    return A, iterNumber, mem

def makeValistandKeys(mem):
    keys = [key for key in mem.keys()]
    vals = [key for key in mem.values()]
    valist = []
    for i in vals:
        c = []
        for j in i:
            c.append(j)
        valist.append(c)
    return keys, valist

def expansion(valist):
    expanded = []
    for i in valist:
        cline = []
        for j in i:
            if j<0:
                idx = j*-1
                j = valist[idx-1]
                for x in j:
                    cline.append(x)
            else:
                cline.append(j)
        expanded.append(cline)
    return expanded

def expansionLoop(valist):
    prevlist = valist
    curlist = expansion(prevlist)
    while prevlist != curlist:
        prevlist = curlist
        curlist = expansion(prevlist)
    return curlist


if __name__=="__main__":
    f = open('toksong.json',) 
    data = json.load(f)
    tdata = data
    iterNumber = -1
    mem ={}
    tData, iterNumber, mem = bpe(tdata, iterNumber, mem)
    keys, valist = makeValistandKeys(mem)
    valist = expansionLoop(valist)
    finaldict = dict(zip(keys, valist)) 
    with open("BPEdict.json", "w") as outfile:  
        json.dump(finaldict, outfile)
    with open("BPEtoksong.json", "w") as outfile:  
        json.dump(tData, outfile)