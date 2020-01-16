import random
import pyperclip #toCopy result in System Clipboard

def getList(n,d):
    xList = []
    for i in range(d):
        xList.append(random.randint(n-200,n+200))
    return xList

while True:
    total = int(input("Total Sum : "))
    elements = int(input("Elements : "))
    total = (total * 100) + random.randint(-50,50)
    print(total)
    mid = int(total/elements) 
    arr = []
    sumArr = []
    possibleList = 100000

    for i in range(possibleList):
        tempList = getList(mid,elements)
        sumArr.append(sum(tempList))
        arr.append(tempList)
        if(sumArr[i]==total):
            break

    print(sumArr.index(min(sumArr, key=lambda x:abs(x-total))))
    tempX = arr[sumArr.index(min(sumArr, key=lambda x:abs(x-total)))]
    tempX[:] = [x / 100 for x in tempX]
    x = '\n'.join(map(str, tempX))
    pyperclip.copy(x)