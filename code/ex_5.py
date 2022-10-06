import numpy as np
import matplotlib.pyplot as plt

fn_ak = lambda k: 2/(k**2 * np.pi**2) * (1 - np.cos(k * np.pi))

ks = np.arange(0, 10)
aks = list(map(fn_ak, ks))
aks[0] = 1/2

plt.plot(ks, aks)
plt.xlabel("k")
plt.ylabel("$A_k$")
plt.show()

fn_true = lambda t, T: 1-2*t/T if t>0 else 1+2*t/T
fn_fourier = lambda t, T, k: fn_ak(k) * np.cos(k * 2 * np.pi * t / T)

ts = np.linspace(-2.5, 2.5, 1000)
y = [fn_true(t, 5) for t in ts]

y0 = np.ones_like(ts) * 1/2
for i in range(1, 10):
    y0 += np.array([fn_fourier(t, 5, i) for t in ts])

plt.plot(ts, y)
plt.plot(ts, y0)
plt.show()
