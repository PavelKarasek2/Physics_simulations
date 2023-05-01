'''
Exercise 1
i=1
sum=0
while i<6:
    i=i+1
    sum=sum+i
    print(sum)
outputs 20
'''

'''
Exercise 2
i = 20
while i > 0:
    print(i)
    i -=2
'''

'''
Exercise 3a
offset = vector(0, -3, 0)
position_now = vector(0, 7, 0)
n = 0
while n < 5:
    rate(1)
    sphere(pos = position_now, color = color.red)
    position_now = position_now + offset
    n = n + 1
The program starts by defining initial values necessary for it. It then moves on into the while loop. Satisfying the condition, it passes the guard, it sets the rate for the execution on the screen
then it creates a sphere, then updates its position by offset, then n is incremented. After it goes through the loop 5 times, n does not pass through the gurad and the loop is over.
'''

'''
Exercise 3b
ball = sphere(pos=vector(-5,0,0), radius = 0.5, color = color.green)
block = box(pos=vector(-8,0,0), color = color.yellow)
velocity = vector(0.4,0.3,0)
dt = 0.1
t = 0
while t < 12:
    rate(50)
    ball.pos = ball.pos + velocity * dt
    t = t + dt
Creates a sphere and a block, defines initial values, continues to while loop, which will be executed until t=12. So it go through it 120 times. The loop itself sets the speed of how we will
see the program executed on the screen. It then updates the position of the sphere and updates time. It moves the sphere opposed to creating a new one because we update its position opposed
to creating a new sphere each time we loop through the code.
'''

'''
Exercise 4
while True:
 rate(100)
 print('Help I am stuck in an infinite loop')
'''

'''
Exercise 5
i=1
sum=0
while i<11:
    sum=sum+i
    i +=1
    print(sum)
It is crucial to increment after updating the sum to get correct result here.
'''

'''
Exercise 6
i=1
sum=0
while sum<55:
    sum=sum+i
    print(i)
    i +=1
In agreement with exercise 5.  
'''
'''
Exercise 7
firstno=1
print(firstno)
secondno=1
print(secondno)
i = 0
while i<28:
    rate(100)
    thirdno= firstno + secondno
    print(thirdno)
    ratio = thirdno/secondno
    print("ratio = ", ratio)
    #get ready to do the next calculation
    firstno= secondno
    secondno= thirdno
    i += 1
'''  

'''
j=20
while j>-20:
    i=-20
    while i<20:
        rate(10)
        sphere(pos=vector(i,j,0), radius=.3)
        i=i+1
    j=j-1
Modified version with more balls, starting in upper left, starting with rows.
'''

'''
Exercise 10
i = 0
while(i<100):
    r=int(random()*10)
    print(r)
    i+=1
Yes, I am getting all numbers
'''
'''
Exercise 11
'''


j=10
while j>-10:
    i=-10
    while i<10:
        rate(20)
        sphere(pos=vector(i,j,0), radius=.3)
        i=i+1
    j=j-1
x1 = int (random()*10)
y1 = int (random()*10)
begin = clock()
redsphere = sphere(pos=vector(x1,y1,0), radius=.3, color = color.red)


choice = True
while (choice == True):
    scene.waitfor('click')
    r = scene.mouse.pos - redsphere.pos
    if mag(r) < .3:
        choice = False
        print("You win")
    else:
        print("Try again")
        
elapsed = clock()
print("You have clicken on the red ball in: ", elapsed)
