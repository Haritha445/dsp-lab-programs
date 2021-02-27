import numpy as np
from matplotlib import pyplot as plt
m=int(input("enter m"));
n1=np.arange(1,500,2);
s=2*np.cos(2*np.pi*(250)*n1+np.pi/2);
z=np.zeros(len(s))
for i in range(0,len(s)):
sum=0;
for k in range(0,m):
if((i-k)>=0):
sum=sum+s[i-k];
z[i]=sum/m;
print(s)
print(z)
plt.subplot(2,1,1);
plt.plot(n1,s);
plt.subplot(2,1,2);
plt.plot(n1,z);
plt.show();10.NOISE
