import numpy as np
import matplotlib.pyplot as plt
from scipy.optimize import minimize

def fn_term(t, T, k): 
    b = 0 if k % 2 == 0 else 2/(np.pi*k)
    return b * np.sin(k * 2 * np.pi * t / T)

def fn_fourier(ts, T, k_max):
    y = np.zeros_like(ts)
    for i in range(1, k_max):
        y += np.array([fn_term(t, T, i) for t in ts])
    return y

T = 5
ks = np.arange(2, 100)
xs1, heights = np.zeros(len(ks)), np.zeros(len(ks))
for i, k_max in enumerate(ks):
    sol = minimize(
        lambda t, k_max: 0.5 - fn_fourier(t, T, k_max), (0,), 
        method="Nelder-Mead", bounds=((0, T/4),), args=(k_max,)
    )
    xs1[i], heights[i] = sol.x, -sol.fun

plt.plot(ks, heights)
plt.xlabel("$k_{max}$")
plt.ylabel("Height")
plt.show()

widths = np.zeros(len(ks))
for i, k_max in enumerate(ks):
    root_first = minimize(
        lambda t, k_max: np.abs(0.5 - fn_fourier(t, T, k_max)), (0,), 
        method="Nelder-Mead", bounds=((0, xs1[i]),), args=(k_max,)
    ).x
    x2 = minimize(
        lambda t, k_max: fn_fourier(t, T, k_max), (xs1[i],), 
        method="Nelder-Mead", bounds=((xs1[i], T/4),), args=(k_max,)
    ).x
    root_second = minimize(
        lambda t, k_max: np.abs(0.5 - fn_fourier(t, T, k_max)), (xs1[i],), 
        method="Nelder-Mead", bounds=((xs1[i], x2),), args=(k_max,)
    ).x
    widths[i] = root_second - root_first

plt.plot(ks, widths)
plt.xlabel("$k_{max}$")
plt.ylabel("Width")
plt.show()
