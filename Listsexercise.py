Web VPython 3.2
'''
sList = []
i = -10
while i <= 10:
    sList.append(sphere(pos=vec(i,0,0), radius = 0.5, color=color.green))
    i = i + 2
    
print(sList[4].pos)

for j in sList:
    rate(1)
    j.color = color.red
'''
'''
numList = [10, 7, 15, 3, 21, 2, 1, 35, 5, 4, 0, 3, 16, 6]

for i in numList:
    if i <= 5:
        print(i)
'''
'''
numList = [10, 7, 15, 3, 21, 2, 1, 35, 5, 4, 0, 3, 16, 6]
numList2 = []

for i in numList:
    if i <= 5:
        numList2.append(i)

print(numList2)
'''
'''
numList = [10, 7, 15, 3, 21, 2, 1, 35, 5, 4, 0, 3, 16, 6]
numList3 = []

for i in numList:
    if i > 6 and i%2==0:
        numList3.append(i)

print(numList3)
'''
'''
myList=[1,1]
for i in range(2,29):
    myList.append(myList[i-2]+myList[i-1])
    
print(myList)
'''
'''
myList = [1,2,3,4,5]
myList2 = myList #these two lists are not independent
myList3 = []
myList3[:]=myList[:] #this list is now a different list
myList.append(6)
print ('myList 2 is ',myList2)
print ('myList 3 is ',myList3)
'''
'''
myList=[1,1]
for i in range(2,29):
    myList.append((myList[i-2]+myList[i-1]))
    
print(myList)
ratioList = []
ratioList[:]=myList[:]

for i in range(2,29):
    ratioList[i] /= myList[i-1]
    
print (ratioList)

results=gdots(color=color.black)
for i in range(0,len(ratioList)):
    results.plot(pos=(i,ratioList[i]))
'''
'''
myList = []
N = 18
for i in range(0, 7, (2/N)*pi):
    myList.append(sphere(pos=vec(5*cos(i),5*sin(i),0), radius = 0.3, color = color.red))
print(myList)

myList2 = []
N = 18
for i in range(0, 7, (2/N)*pi):
    myList.append(sphere(pos=vec(5*cos(i),0,5*sin(i)), radius = 0.3, color = color.blue))
print(myList2)
'''
'''
#expect 20 and nothing else
x = 5
if x < 20:
    print('x is less than 20,')
elif x < 10:
    print('x is less than 10')
else:
    print('x is greater than 20')
'''
'''
score = 45

if score < 60:
    grade ='F'
elif score < 70:
    grade ='D'
elif score < 80:
    grade ='C'
elif score < 90:
    grade ='B'
elif score == 100:
    grade = 'A+'
else:
    grade ='A'
print(grade)
'''
'''
#Euler 1
sum = 0
for i in range(1,1000):
    if i %3 == 0 or i %5 == 0:
        sum += i
print(sum)
'''
#Euler 2
myList=[1,1]
i=0
while(myList[i-1]<4000000):
    myList.append(myList[i-2]+myList[i-1])
    i += 1
    
print(myList)

sum = 0
for i in myList:
    if i%2 == 0:
        sum +=i
    
print(sum)
