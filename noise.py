import numpy as np
from matplotlib import pyplot as plt
j=(-1)**(0.5)
w=np.arange(-1*np.pi,np.pi,0.01*np.pi)
s=20*np.random.rand(500)
x=[]
for i in range(0,len(w)):
sum=0
for n in range(0,len(s)):
sum=sum+s[n]*np.exp(-1*j*w[i]*n)
x.append(sum)
plt.subplot(2,1,1)
plt.plot(w,np.abs(x))
plt.subplot(2,1,2)
plt.plot(w,np.angle(x))
plt.show();
