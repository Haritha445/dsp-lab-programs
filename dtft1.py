import numpy as np
from matplotlib import pyplot as plt
m=np.arange(0,500)
F=250;Fs=10000;
x=np.cos(2*np.pi*(F/Fs)*m)
X=[]
w=np.arange(-1*np.pi,np.pi,0.01*np.pi)
for i in range(0,len(w)):
	s=0
	for n in range(0,len(x)):
		s=s+x[n]*np.exp(-1*1j*w[i]*n);
	X.append(s)
	X[i]=s;
plt.subplot(2,1,1)
plt.plot(w,np.abs(X))
plt.subplot(2,1,2)
plt.plot(w,np.angle(X))
plt.show()
