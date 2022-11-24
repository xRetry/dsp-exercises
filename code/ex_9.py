import numpy as np
import matplotlib.pyplot as plt


def signal_function(t):
    """Function of the given signal"""
    f1, f2 = 90, 110 # Hz
    return np.sin(2*np.pi*f1*t) + np.sin(2*np.pi*f2*t)


def add_signal(axs, t_min, t_max, num_pts, style="-", plot_fft=True):
    """Helper function to add data to the current row of subplots"""

    # Creating signal
    t = np.linspace(t_min, t_max, num_pts)
    y = signal_function(t)

    # Adding to time domain plot
    axs[0].plot(t, y, style)

    if plot_fft:
        # Computing the FFT
        fft = np.abs(np.fft.fft(y))
        # Creating the corresponding frequency values
        freq = np.arange(len(fft)) / (t_max - t_max) # divided by duration
        # Removing parts beyond the nyquist frequency
        fft = fft[:int(len(fft)/2)]
        freq = freq[:int(len(freq)/2)]

        # Adding to frequency domain plot
        axs[1].stem(freq, fft, use_line_collection=True)


def plot_signals():
    # Given sampling frequencies
    fs = [40, 80, 100, 125] # Hz

    # Creating subplots
    _, axs = plt.subplots(len(fs), 2, sharex='col', figsize=(12, 12))
    # Iterating over sampling frequencies
    for i, f in enumerate(fs):
        # Adding true signal to subplot
        add_signal(axs[i], 0, 0.1, 1000, plot_fft=False)
        # Adding sampled signal to subplot
        add_signal(axs[i], 0, 1, f, "o-")
        # Configuring current row of subplots
        axs[i, 0].set_xlim([0, 0.1])
        axs[i, 0].set_ylabel(f"Sampling Frequency: {f} Hz")
        axs[i, 0].set_yticks([])
    
    # Configuring first and last subplot
    axs[0, 0].set_title("Time Domain")
    axs[0, 1].set_title("Frequency Domain")
    axs[-1, 0].set_xlabel("Time [s]")
    axs[-1, 1].set_xlabel("Frequency [Hz]")
    # Showing figure
    plt.tight_layout()
    plt.show()


if __name__ == "__main__":
    plot_signals()
