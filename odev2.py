x=0
x1=2
x2=4
sayac=0

while sayac < 4:
    xk=(x1+x2)/2
    x=xk
    f=x*x*x-2*x*x-5
    if(f<0):
        x1=xk
    else:
        x2=xk
    sayac += 1

print("4 iterasyon sonucu bulunan kok",xk)
print("4 iterasyon sonucu buluanan deger",f)