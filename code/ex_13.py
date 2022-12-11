import numpy as np
import matplotlib.pyplot as plt

f = np.linspace(0, 0.5, 300)

H_11 = 1/2 * (1 + np.cos(f*2*np.pi))
H_13 = (1 + np.cos(f*2*np.pi)) / (4 - 2 * np.exp(1j*f*2*np.pi))

plt.figure()
plt.plot(f, H_11, label="FIR from 11b")
plt.plot(f, H_13, label="IIR from 13")
plt.title("Amplitude of FIR and IIR filter")
plt.xlabel("Normalized Frequency [cycles/sample]")
plt.ylabel("Amplitude")
plt.legend()
plt.show()
