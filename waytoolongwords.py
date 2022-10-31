words=int(input())
allwords=[]
for w in range(words):
    aword=input()
    if len(aword)>10:
        allwords.append(aword[0]+str(len(aword)-2)+aword[-1])
    else:
        allwords.append(aword)
        
for w in allwords:
    print(w)