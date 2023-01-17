import numpy as np
import matplotlib.pyplot as plt

def plot_frequency_response():
    w = np.logspace(-1, 1, 500)
    angles = np.linspace(0, np.pi/2, 7)
    zero1 = 0 + 0j
    zero2 = 0 + 0j

    fig, axs = plt.subplots(1, 2, figsize=(12, 6))
    for i in range(len(angles)):
        pole1 = 1 * np.exp(1j*angles[i])
        pole2 = 1 * np.exp(-1j*angles[i])

        F = (1j*w - zero1) * (1j*w - zero2) / ((1j*w-pole1) * (1j*w-pole2))

        axs[0].loglog(w, abs(F), label=f"{round(np.rad2deg(angles[i]))} deg")
        axs[1].semilogx(w, np.angle(F, deg=True), 
            label=f"{round(np.rad2deg(angles[i]))} deg"
        )

    axs[0].set_title("Amplitude of the Frequency Response")
    axs[0].set_xlabel("$\omega$ [$s^{-1}$]")
    axs[0].set_ylabel("Amplitude")
    axs[0].legend(title="Poles")

    axs[1].set_title("Phase of the Frequency Response")
    axs[1].set_xlabel("$\omega$ [$s^{-1}$]")
    axs[1].set_ylabel("Phase [deg]")
    axs[1].legend(title="Poles")

    plt.tight_layout()
    plt.show()

if __name__ == "__main__":
    plot_frequency_response()
