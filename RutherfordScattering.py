mAP = 4*1.67e-27
mGN = 197*1.67e-27
cAP = 2*1.6e-19
cGN = 79e-19
rAP = 1e-15
rGN = 6e-15
rInit = vector(-3e-13,1e-14,0)
#graphs
X_momentum = gdisplay(xtitle = 'Time', ytitle= 'Px',height=200)
Alphapx = gcurve(color = color.cyan)
Aupx = gcurve(color=color.yellow)
totalpx = gcurve(color = color.green)
Y_momentum = gdisplay(xtitle = 'Time', ytitle = 'Py',height=200)
Alphapy = gcurve(color = color.cyan)
Aupy = gcurve(color=color.yellow)
totalpy = gcurve(color= color.green)
#prepare the display
displaymax = 10
scene.range = displaymax
physicalmax = mag(rInit)
scalefactor = displaymax/physicalmax
#create the spheres
alphaParticle = sphere(pos = scalefactor*rInit, radius = 3*scalefactor*rAP, color = color.red, make_trail = True)#3times larger radius then it should have
goldenNucleus = sphere(pos = vector(0,0,0), radius = scalefactor*rGN, color = color.yellow, make_trail = True)
pAP = vector(1e-19,0,0)
pGN = vector(0,0,0)
deltaT = (2*mag(rInit)/(mag(pAP)/mAP))/1000
t = 0
R = -rInit
b = rAP+rGN
while t<1000 and mag(alphaParticle.pos) <= 1.1*mag(scalefactor*rInit):
    rate(100)
    alphaParticle.pos += scalefactor*(pAP/mAP)*deltaT
    goldenNucleus.pos +=scalefactor*(pGN/mGN)*deltaT
    F_GonA = -(9e9)*((cAP*cGN)/mag(R)**2)*(R/mag(R))
    pAP += F_GonA*deltaT
    pGN += (-F_GonA)*deltaT
    R = (goldenNucleus.pos - alphaParticle.pos)/scalefactor
    t += deltaT
    Alphapx.plot(pos=(t,pAP.x))
    Alphapy.plot(pos=(t,pAP.y))  
    Aupx.plot(pos=(t,pGN.x))
    Aupy.plot(pos=(t,pGN.y))
    totalpx.plot(pos=(t,pGN.x+pAP.x))
    totalpy.plot(pos=(t,pGN.y+pAP.y))