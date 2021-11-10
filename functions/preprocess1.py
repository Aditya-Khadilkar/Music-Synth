import json
def seperator(filename):
    f = open(filename, 'r')
    ls = f.readlines()
    finalElementList = []
    for i in ls:
        i = i.replace(" ", "")
        #i = i.replace("|", "")
        i = i[0:-2]
        elementLine = []
        inside = False
        curElement = ''
        for j in i:
            #print(j)
            if j =='|':
                elementLine.append(curElement)
                curElement = ''
                curElement = curElement + j
                elementLine.append(curElement)
            elif j==']' and inside:
                curElement = curElement + j
                inside = False
            elif inside:
                curElement = curElement + j
            elif j=='[' and not inside:
                if len(curElement) != 0:
                    #print(curElement)
                    elementLine.append(curElement)
                    curElement = ''
                    curElement = curElement + j
                    inside = True
                else:
                    curElement = ''
                    curElement = curElement + j
                    inside = True

            elif not inside and j.isalpha() == False:
                curElement = curElement + j
            elif not inside and j.isalpha():
                #print(curElement)
                elementLine.append(curElement)
                curElement = ''
                curElement = curElement + j
            else:
                print('printing j: '+j)
        elementLine.append('%')
        finalElementList.append(elementLine)
    return finalElementList

def dictGenerator(finalElementList):
    flat_list = [item for sublist in finalElementList for item in sublist]
    setOfEle = list(set(flat_list))
    eleDict ={}
    for i in range(len(setOfEle)):
        eleDict.update({i:setOfEle[i]})
    word2tok = {v: k for k, v in eleDict.items()}
    vn = word2tok['%']
    k0 = eleDict[0]
    word2tok[k0] = vn
    word2tok['%'] =0
    tok2word = {v: k for k, v in word2tok.items()}
    toksong = []
    for i in flat_list:
        tok = word2tok[i]
        toksong.append(tok)
    return word2tok, tok2word, toksong

if __name__ == '__main__':
    ls = seperator('refrain.txt')
    word2tok, tok2word, toksong = dictGenerator(ls)
    with open('word2tok.json', 'w') as fp:
        json.dump(word2tok, fp)
    with open('tok2word.json', 'w') as fp:
        json.dump(tok2word, fp)
    with open('toksong.json', 'w') as fp:
        json.dump(toksong, fp)