def SpiralOut (n):
    if n == 0:
        return 0
    elif n ==1 or n==2:
        return 1
    else:
        return SpiralOut(n-1) + SpiralOut(n-2) 

for i in range(5):
    print (SpiralOut(i))

import time
t_n = []
n = []

for i in range (40):
    n.append(i)
    t0 = time.time()
    result = SpiralOut(i)
    t1 = time.time()
    print (t1 - t0)
    t_n.append(t1-t0)

print (n, t_n)

import matplotlib.pyplot as plt
plt.plot(n, t_n)
plt.show()
