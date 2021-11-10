def cutHead(ls):
    head = ''
    songParts = []
    cursection = ''
    for i in ls:
        if i=='':
            pass
        elif i.startswith('%%'):
            head = head + i  
        elif i.startswith('V:'):
            if cursection != '':
                songParts.append(cursection)
            head = head + i
            head = head + '<New Voice here> \n' 
        elif i[1] ==':':
            head = head +i
            #head = head + '\n'
        else:
            cursection = cursection+i
            #head = head + '<no line here>\n'
    songParts.append(cursection)
    
    return head, songParts


def writeVerses(ls):
    for i in range(len(ls)):
        verse = ls[i]
        name = 'verse'+ str(i+1) + '.txt'
        f = open('tempfilesm/'+name,'w')
        f.write(verse)

def activateBoilerplate(songname):
    f = open(songname,'r')
    ls = f.readlines()
    head, songparts = cutHead(ls)
    f = open('tempfilesm/head.txt','w')
    f.write(head)
    writeVerses(songparts)


if __name__== "__main__":
    activateBoilerplate('Neon-Genesis-Evangelion-op.abc')

