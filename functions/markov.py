import json
import numpy as np
import random

def loadData(jsonfile):
    f = open(jsonfile,'r') 
    data = json.load(f)
    setDict = {k: v for v, k in enumerate(set(data))}
    setinv = {v: k for k, v in setDict.items()}
    tdata = data
    indexed =[]
    for i in tdata:
        val = setDict[i]
        indexed.append(val)
        
    return setinv, indexed

def makeMatrix(indexed):
    matrix = np.zeros((len(set(indexed)),len(set(indexed))))
    for i in range(len(indexed)-1):
        cur = indexed[i]
        to = indexed[i+1]
        matrix[cur][to] = 1
    return matrix

def generateSeed(index,size):
#vocabsize = setinv.length
    seed = np.zeros((1,size))
    seed[0][index] = 1
    return seed

def chooseElement(res):
    choices=[]
    for i in range(res.shape[1]):
        if res[0][i] >0:
            choices.append(i)

    ans = random.choices(choices)
    return ans[0]

def markovLoop(noOfTokens):
    generated = []
    setinv, indexed = loadData('tempfilesm/BPEtoksong.json')
    print(indexed)
    size = len(setinv)
    matrix = makeMatrix(indexed)
    index = random.randint(0,len(setinv))
    for i in range(noOfTokens):
        generated.append(index)
        seed = generateSeed(index,size)
        res = np.dot(seed,matrix)
        index = chooseElement(res)
    BPEtokens = [setinv[k] for k in generated]
    with open("tempfilesm/generated.json", "w") as outfile:  
        json.dump(BPEtokens, outfile)
    #return BPEtokens

if __name__ == '__main__':
    markovLoop(200)
    