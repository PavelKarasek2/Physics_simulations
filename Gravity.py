
G = 6.7e-11 #Gravitational constant in N m2/kg2
mplanet = 6e24 #Mass of planet (Earth) in kg
rplanet = 6.4e6 #Radius of planet (Earth) in meters
mcraft = 15e3 #Mass of spacecraft in kg

planetstart = vector(0,0,0) #location of planet
craftstart = vector(-13e7, 6.5e7, 0) #initial location of the spacecraft in meters

displaymax = 10
scene.range = displaymax

physicalmax = mag(craftstart)
scalefactor = displaymax/physicalmax 

planet = sphere(pos=planetstart*scalefactor, radius=1, texture="https://i.imgur.com/do31Gdf.jpg")

craft = sphere(pos=craftstart*scalefactor, radius = 0.2, color = color.red) #creating a spacecraft

planet.physpos = planetstart # adds an attribute to the planet object which represents its actual physical location in meters
craft.physpos = craftstart # adds an attribute to the craft object which represents its actual physical location in meters

#Initial calculations
r = craft.physpos - planet.physpos
rmag = mag(r)
F = -G*mplanet*mcraft/(rmag**2)
rhat = r/rmag
Fg = F*rhat #gravitational force the Earth pulls on the planet

print('The force is ',F,' at position ',r)
F0 = 2*mag(Fg) #magnitude of initial force
fscale = 1/F0 #calculate scalefactor

Force_arrow = arrow(pos=craft.pos, axis = Fg*fscale, color = color.blue)

while craft.physpos.x<13e7:
    rate(1) #slow the display to one per second
    craft.physpos.x=craft.physpos.x + 6.5e7 #update the actual craft position. #Note we are only changing its x component.

    #Paste in here all your code from parts 1-5
    r = craft.physpos - planet.physpos
    rmag = mag(r)
    F = -G*mplanet*mcraft/(rmag**2)
    rhat = r/rmag
    Fg = F*rhat
    #This is necessary to update the force
    #update the display
    craft.pos = craft.physpos*scalefactor #updates craft position on screen
    #create a new arrow representing the force
    Force_arrow = arrow(pos=craft.pos, axis = Fg*fscale, color = color.blue)
