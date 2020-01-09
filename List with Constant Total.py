import random

def getList(n,d):
    xList = []
    for i in range(d):
        xList.append(random.randint(n-200,n+200))
    return xList

total = int(input("Total Sum : "))
elements = int(input("Elements : "))
mid = int(total/delements)
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
print(tempX)

myFile=open('output.txt','w')
for element in tempX:
    myFile.write(str(element))
    myFile.write('\n')
myFile.close()