import numpy as np
from scipy import signal
import matplotlib.pyplot as plt

L=51 #L-point filter
b = (np.ones(L))/L #numerator co-effs of filter transfer function
a = np.ones(1)  #denominator co-effs of filter transfer function

w, h = signal.freqz(b,a)
plt.subplot(2, 1, 1)
plt.plot(w, 20 * np.log10(abs(h)))
plt.ylabel('Magnitude [dB]')
plt.xlabel('Frequency [rad/sample]')

plt.subplot(2, 1, 2)
angles = np.unwrap(np.angle(h))
plt.plot(w, angles)
plt.ylabel('Angle (radians)')
plt.xlabel('Frequency [rad/sample]')
plt.show()
