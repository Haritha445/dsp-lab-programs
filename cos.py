import numpy as np
from matplotlib import pyplot as plt
F=250;Fs=10000;
n=np.arange(0,500);
s1=0.5*np.cos(2*np.pi*F/Fs*n+np.pi/2);
s2=1.5*np.cos(2*np.pi*F/Fs*n+np.pi/2);
s=s1+s2;
plt.subplot(3,1,1);
plt.stem(n,s1);
plt.subplot(3,1,2);
plt.stem(n,s2);
plt.subplot(3,1,3);
plt.stem(n,s);
plt.show();
