import random
#define class competitor
class competitor:
    def __init__(obj, number, balance=1):
        obj.number = number
        obj.balance = balance
#ask user how many rounds of the game should be played
n = input('How many rounds?')
n = int(n)
print('You chose ', n, ' rounds')
#create objects and lists
#ci stands for competitor of inner circle, co for competitor of outer circle

ci0 = competitor(0)
ci1 = competitor(1)
ci2 = competitor(2)
ci3 = competitor(3)
ci4 = competitor(4)
co0 = competitor(0)
co1 = competitor(1)
co2 = competitor(2)
co3 = competitor(3)
co4 = competitor(4)

inner = [ci0, ci1, ci2, ci3, ci4]
outer = [co0, co1, co2, co3, co4]

#create spheres for visualization
#ci0sphere = sphere( 
#Outer loop
for y in range(n):
#One round of rock paper scissors
    for i in range(5):
        x = random.random()
    #outer wins
        if x < 1/3:
        #check that loser has money and execute accordingly
            if outer[i].balance > 0:
                outer[i].balance -= 1
                inner[i].balance += 1
    #inner wins
        elif x > 2/3:
            if inner[i].balance > 0:
                inner[i].balance -= 1
                outer[i].balance += 1
#inner circle rotation
    temp = inner[4]
    for j in range(4,0,-1):
        inner[j] = inner[j-1]
    inner[0] = temp
#print results
    print('Results for round y:')
    for i in range(5):
        print('balance of co',i, ':', outer[i].balance, '$')
    for initPos in range(5):
        final = (initPos + n) % 5
        print('balance of ci',initPos,':', inner[final].balance, '$')