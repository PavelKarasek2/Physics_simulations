
graph = gdisplay(title='Position of spacecraft', xtitle = 'time (s)', ytitle = 'x position (m)')
posgraph = gcurve(color=color.red)

graph2 = gdisplay(title='Energy of spacecraft', xtitle = 'separation', ytitle = 'Energy (J)')
kingraph2 = gcurve (color=color.blue,  dot=True)
potgraph2 = gcurve (color = color.yellow,  dot=True)
totgraph2 = gcurve (color = color.green,  dot=True)
#constants
G = 6.7e-11
mEarth = 6e24
rEarth = 6.4e6
mcraft = 15e3
Earthstart = vector(0,0,0)
craftstart = vector(-10*rEarth, 0, 0)
mMoon = 7e22 
rMoon = 1.75e6
Moonstart= vector(4e8, 0, 0) 
dt =10

#prepare display
displaymax = 10
scene.range = displaymax
physicalmax = mag(Moonstart)
scalefactor = displaymax/physicalmax

#create display objects
Earth = sphere (pos = Earthstart, radius = rEarth*scalefactor, texture = "https://i.imgur.com/do31Gdf.jpg")
Earth.physpos = Earthstart
craft = sphere(pos = craftstart*scalefactor, radius = .1, color = color.yellow, make_trail=True)
craft.physpos = craftstart
Moon = sphere (pos = Moonstart*scalefactor, radius = rMoon*scalefactor, color = color.red)
Moon.physpos = Moonstart


#initial values
vcraft = vector(0, 3.27e3, 0) #initial velocity is straight up along y
pcraft = mcraft*vcraft
t = 0



while t < 60*24*60*60:
    rate(6000) # slow down 
    #Updating position by iteration by r_new = r_initial + (p_initial/m_craft)*dt
    craft.physpos = craft.physpos + (pcraft/mcraft)*dt #use momentum principle to update actual position of the spacecraft
    t = t+dt #updating time - that is what the while loop checks for every time
    #interaction of Earth on spacecraft
    r_es = craft.physpos - Earth.physpos #relative position of spacecraft to Earth
    rmag_es = mag(r_es) #the distance between the Earth and the spacecraft
    F_es = -G*mEarth*mcraft/(rmag_es**2) #magnitude of force of Earth on spacecraft
    rhat_es = r_es/rmag_es #unit vector in the direction of r_es
    Fg_es = F_es*rhat_es #force of Earth on spacecraft
    #check on crash Earth spacecraft
    if rmag_es<=rEarth:
        break
    #interaction of Moon on spacecraft
    
    r_ms = craft.physpos - Moon.physpos #relative position of spacecraft to Moon
    rmag_ms = mag(r_ms) # distance between Moon and Spacecraft
    F_ms = -G*mMoon*mcraft/(rmag_ms**2) #magnitude of force Moon and spacecraft act on each other
    rhat_ms = r_ms/rmag_ms #unit vector in the direction of r_ms
    Fg_ms = F_ms*rhat_ms #force on spacecraft by Moon
   
    #check on crash Moon spacecraft
    if rmag_ms <= rMoon:
        break
    #Energy 
    kinetic = (1/2)*((mag(pcraft)/mcraft)**2)*mcraft
    kingraph2.plot(pos=(t,kinetic))
    potential = -G*mEarth*mcraft/rmag_es-G*mMoon*mcraft/rmag_ms
    potgraph2.plot(pos=(t,potential))
    total = kinetic + potential
    totgraph2.plot(pos=(t,total))
    #net force on the spacecraft
    Fnet = Fg_ms + Fg_es
    #new momentum of the spacecraft => will be used in next iteration
    pcraft = pcraft + Fnet*dt
    #updating spacecraft position
    craft.pos = craft.physpos*scalefactor
    posgraph.plot(pos=(t, craft.physpos.x))
    
    
    #3.28e3 makes it crash to moon right away
    #3.34e3 ellipse around moon
    #3.27417e3 figure 8 and then crash on moon
    
    #When the spaceship comes close to a stop, it loses all its initial momentup and velocity and the gravitational forces give it a new momentum and velocity
    
    #10 s time steps produces same results as 2s time steps in my eyes.
    #1000s time step produces tremendously inaccurate results