myball=sphere(pos=vec(-4,-3,0), radius=.2, color=color.blue, make_trail=True)
myball.v=vector(1,1,0)

wall=box(pos=vec(0,0,0),axis=vec(-3,2,0),height=.1, width=.01, color=color.red)
wall2 = box(pos=vec(0,0,0),axis=vec(-7,-4,0),height=.1, width=.01, color=color.red)

def slope(direction):
    m = direction.y/direction.x #slope
    return (m)
    
def b(direction, position):
     b = position.y-(direction.y/direction.x)*position.x #x=0
     return(b)

def intercept(m1, b1, m2, b2):
    x_intercept = (b2-b1)/(m1-m2)
    intercept = vec((x_intercept),(m1*x_intercept+b1),0)
    return (intercept)

coll_point = intercept(slope(myball.v), b(myball.v, myball.pos), slope(wall.axis), b(wall.axis,wall.pos))
print(coll_point)
myball.pos = coll_point

def bounce(v0,wallvec):
 return 2*dot(v0,norm(wallvec))*norm(wallvec)-v0

rate(6000)

scene.waitfor('click') 
myball.v = bounce(myball.v,wall.axis)
myball.pos += myball.v

coll_point2 = intercept(slope(myball.v), b(myball.v, myball.pos), slope(wall2.axis), b(wall2.axis,wall2.pos))
print(coll_point2)
myball.pos = coll_point2

scene.waitfor('click') 
myball.v = bounce(myball.v,wall2.axis)
myball.pos += myball.v