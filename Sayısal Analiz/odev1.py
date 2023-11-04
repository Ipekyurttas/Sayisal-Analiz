import math
x0=0
x=math.pi/5
f1 = math.cos(x0)-math.sin(x0)*(x-x0)
kesme1 = math.cos(x) - f1
f2 = math.cos(x0)-math.sin(x0)*(x-x0)-math.cos(x0)*(x-x0)*(x-x0)/2
kesme2 = math.cos(x) - f2
print("Taylor Serisi Bir Terimli Kesme Hatası",kesme1)
print("Taylor Serisi İki Terimli Kesme Hatası",kesme2)