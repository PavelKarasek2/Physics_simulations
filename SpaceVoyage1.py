G = 6.7e-11
mEarth = 6e24
rEarth = 6.4e6
mcraft = 15e3
planetstart = vector(0,0,0)
craftstart = vector(-10*rEarth, 0, 0)
dt =60

#prepare display
displaymax = 10
scene.range = displaymax
physicalmax = mag(craftstart)
scalefactor = displaymax/physicalmax

#create display objects
Earth = sphere (pos = planetstart, radius = rEarth*scalefactor, texture = "https://i.imgur.com/do31Gdf.jpg")
Earth.physpos = planetstart
craft = sphere(pos = craftstart*scalefactor, radius = .1, color = color.yellow, make_trail=True)
craft.physpos = craftstart

#initial values
vcraft = vector(0, 2e3, 0) #initial velocity is straight up along y
pcraft = mcraft*vcraft
t = 0

#CALCULATION LOOP: ALL REPEATED CALCULATIONS GO INSIDE THE LOOP
while t < 10*365*24*60*60:
    rate(100) # slow down motion to make animation look nicer
    #We're going to put in the effect of gravity here
    craft.physpos = craft.physpos + (pcraft/mcraft)*dt #use momentum principle to update actual position of the spacecraft
    t = t+dt
    r = craft.physpos - Earth.physpos
    rmag = mag(r)
    F = -G*mEarth*mcraft/(rmag**2)
    rhat = r/rmag
    Fg = F*rhat
    pcraft = pcraft + Fg*dt
    craft.pos = craft.physpos*scalefactor