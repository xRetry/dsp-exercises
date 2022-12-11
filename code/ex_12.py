import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(0, 0.5, 300)

H = 1/8 * (1 - np.cos(f*4*np.pi))

plt.figure()
plt.plot(f, H)
plt.title("Amplitude of the FIR filter from example 12")
plt.xlabel("Normalized Frequency [cycles/sample]")
plt.ylabel("Amplitude")
plt.show()
