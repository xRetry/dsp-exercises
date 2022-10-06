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

fn_term = lambda t, T, k: fn_ak(k) * np.cos(k * 2 * np.pi * t / T)

def fn_fourier(ts, k_max, T):
    y = np.ones_like(ts) * 1/2
    for i in range(1, k_max+1):
        y += np.array([fn_term(t, T, i) for t in ts])
    return y

T = 5
ts = np.linspace(-T, T, 1000)

plt.plot(ts, fn_fourier(ts, 1, T), label="$k_{max}=1$")
plt.plot(ts, fn_fourier(ts, 9, T), label="$k_{max}=9$")
plt.xticks([-T, 0, T], ["$-T_0$",0 , "$T_0$"])
plt.ylabel("$f(x)$")
plt.legend()
plt.show()
