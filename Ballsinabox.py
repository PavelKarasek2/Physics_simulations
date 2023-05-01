
ball1 = sphere(pos=vector(-5,0,0), radius=2, color=color.cyan)
ball2 = sphere(pos=vector(5,0,0), radius = 2, color= color.white)
Ceiling = box(pos=vector(0,6,0), size=vector(12,0.2,12),color = color.red)
Floor = box(pos=vector(0,-6,0), size=vector(12,0.2,12), color = color.red)
wallR = box(pos=vector(6,0,0), size=vector(0.2,12,12), color=color.green)
wallL = box(pos=vector(-6,0,0), size = vector(0.2,12,12), color = color.green)
wallback = box(pos=vector(0,0,-6), size = vector(12,12,0.2), color = color.yellow)

ball1.velocity = vector(25,5,15)
ball1.trail = curve(color=color.blue)

ball2.velocity = vector(5, 20, 10)
ball2.trail = curve(color=color.purple)

vscale = 0.1
varr = arrow(pos=ball1.pos, axis=vscale*ball1.velocity, color=color.blue)
varr2 = arrow(pos=ball2.pos, axis=vscale*ball2.velocity, color=color.purple)
deltat = 0.005
t = 0
scene.autoscale = False

#Ball1 bouncing off the wall
while True:
    rate(100)
    varr.pos = ball1.pos
    if ball1.pos.x > wallR.pos.x:
        ball1.velocity.x = - ball1.velocity.x
    if ball1.pos.x < wallL.pos.x:
        ball1.velocity.x= - ball1.velocity.x
    if ball1.pos.y < Floor.pos.y:
        ball1.velocity.y= - ball1.velocity.y
    if ball1.pos.y > Ceiling.pos.y:
        ball1.velocity.y= - ball1.velocity.y
    if ball1.pos.z < wallback.pos.z:
        ball1.velocity.z = - ball1.velocity.z
    if ball1.pos.z > 6:
        ball1.velocity.z = - ball1.velocity.z
    varr.axis = vscale*ball1.velocity
    ball1.pos = ball1.pos + ball1.velocity*deltat
    ball1.trail.append(pos=ball1.pos)
    varr2.pos = ball2.pos
    if ball2.pos.x > wallR.pos.x:
        ball2.velocity.x = - ball2.velocity.x
    if ball2.pos.x < wallL.pos.x:
        ball2.velocity.x= - ball2.velocity.x
    if ball2.pos.y < Floor.pos.y:
        ball2.velocity.y= - ball2.velocity.y
    if ball2.pos.y > Ceiling.pos.y:
        ball2.velocity.y= - ball2.velocity.y
    if ball2.pos.z < wallback.pos.z:
        ball2.velocity.z = - ball2.velocity.z
    if ball2.pos.z > 6:
        ball2.velocity.z = - ball2.velocity.z
    varr2.axis = vscale*ball2.velocity
    ball2.pos = ball2.pos + ball2.velocity*deltat
    ball2.trail.append(pos=ball2.pos)
    if ball1.pos==ball2.pos:
        ball1.velocity = ball2.velocity
        ball2.velocity = ball1.velocity