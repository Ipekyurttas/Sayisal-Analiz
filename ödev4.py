import math
x=2
sayac=0

while sayac < 4:
    f=4*(math.e**(-0.5*x))-x
    f1=-2*(math.e**(-0.5*x))-1
    xk=x-(f/f1)
    x=xk
    sayac += 1

print("4 iterasyon sonucu bulunan kok",xk) 