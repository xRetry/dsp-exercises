import numpy as np
import matplotlib.pyplot as plt


def plot():
    hs = np.array([
        [1/3, 1/3, 1/3],
        [1/4, 1/2, 1/4],
        [-1/4, 1/2, -1/4]
    ])

    omega = np.linspace(0, np.pi, 500)
    labels = ["11a", "11b", "11c"]
    plt.figure()
    for i, h in enumerate(hs):
        H = h[1] + 2*h[2] * np.cos(omega)
        plt.plot(omega, H, label=f"Exercise {labels[i]}")

    plt.title("Amplitude of the FIR filters")
    plt.xlabel(r"$\omega$ [rad]")
    plt.ylabel("Amplitude")
    plt.legend()
    plt.show()


if __name__ == "__main__":
    plot()
