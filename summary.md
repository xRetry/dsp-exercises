# 2. Fourier Series

Any piecewise continuous, bounded and **periodic** function can be represented as a Fourier Series.

```math
  f(t) = \sum_{k=0}^\infty \left( A_k \cos(k\omega_0t) + B_k \sin(k\omega_0t) \right)
```

Alternatively with amplitude and phase:

```math
  f(t) = \sum_{k=0}^\infty a_k \cos(k\omega_0t - \phi_k)
```

As complex valued exponential:

$$ \begin{equation}
  f(t) = \sum_{k=-\infty}^{\infty} \left( F_k e^{ik\omega_0t} \right)  
\end{equation} $$

- sin and cos are orthogonal basis functions
- There is no information about frequencies between $k\omega_0$ and $(k+1)\omega_0$.
Therefore, $\omega_0$ is also the sampling interval.
The longer $T_0$, the smaller $\omega_0$ and the better the frequency resolution.
- Even signal $\Rightarrow$ zero phase

> TODO: Add coefficiants formulas

$$ \begin{equation}
  F_k = \frac{1}{T_0} \oint f(t) e^{-ik\omega_0t} dt
\end{equation} $$

- An extra formula for $A_0$ is required, because of the factor 2.
- Fourier analysis: computing $A_k$ and $B_k$ from $f(t)$
- Fourier synthesis: computing $f(t)$ from $A_k$ and $B_k$
- When all $k$ are accounted for, analysis followed by synthesis is a no-op

> TODO: Time shift

- Kinks in the function require many $k$s for a good fit
- Steps require even more $k$s and lead to the Gibbs phenomenon:
There persists an overshoot, but the overshoot duration decreases.

> TODO: Hermitian symmetry

Conversion between coefficiants:

$$ \begin{align}
  a_0 &= \sqrt{A_0^2} = \sqrt{F_0 F_0*} \\
  a_k &= \sqrt{A_k^2 + B_k^2} = 2 \sqrt{F_k F_k^*} \\
  \phi_k &= \text{atan}\frac{B_k}{A_k} = - \text{atan}\frac{Im\{F_k\}}{Re\{F_k\}}
\end{align} $$ 

# 3. Fourier Transform

- Results from the Fourier Series, if the considered time interval goes to infinity ($T_0 \rightarrow \infty$).
- Applies to **non-periodic** functions

$$ \begin{align}
  F(\omega) &= \int_{-\infty}^{\infty} f(t) e^{-i\omega t} dt \\
  f(t) &= \frac{1}{2\pi} \int_{-\infty}^{\infty} F(\omega) e^{i \omega t} d\omega
\end{align} $$

Differentiation in time domain becomes multiplication in frequency domain:

$$ \begin{align}
  \frac{d}{dt} f(t) &\rightarrow i\omega F(\omega)\\
  \int f(t) &\rightarrow \frac{1}{\omega} F(\omega)
\end{align} $$

Convolution in time domain becomes multiplication in frequency domain:

$$ \begin{align}
  h(t) &= f(t) \star g(t) = \int_{-\infty}^\infty f(\tau) g(t - \tau) d\tau\\
  H(\omega) &= F(\omega) G(\omega)
\end{align} $$

> TODO: Correlation

> TODO: Plancherel's theorem

> TODO: Parseval's theorem

**Dirac delta function**

The Dirac delta function ($\delta(t)$) can be used to pick a value at a specific time in an integral.
In the frequency domain, the $\delta$-function becomes 1 (same across all frequencies).

$$ \begin{align}
  \delta(t) &\rightarrow 1\\
  2 \pi \delta(\omega) &\rightarrow 1
\end{align} $$

Duality theorem:

$$ \begin{align}
  f(t) &\leftrightarrow F(\omega) \\
  F(t) &\leftrightarrow 2 \pi f (-\omega)
\end{align} $$

Except for $2\pi$ and the inversion, the two members of the Fourier pair are interchangable.

**Heaviside step function**

The delta function is very important, but physically not realizeable (infinite amplitude).
The step function is a way around this.

$$ \begin{equation}
  FT\[u(t)\] = \frac{1}{i\omega} + \pi \delta(\omega)
\end{equation} $$

**Sign function**

The sign function is not square integrable and cannot be Fourier transformed.
However, with a limit-process:

$$ \begin{equation}
  FT\[sgn(t)\] = \frac{2}{i\omega}
\end{equation} $$

**Boxcar function**

$$ \begin{align}
  F(\kappa) &= T_0 \frac{\sin(\kappa)}{\kappa}\\
  \kappa &= \frac{\omega T_0}{2}
\end{align} $$

**Gaussian distribution**

$$ \begin{align}
  f(t) &= \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{t^2}{2\sigma^2}}\\
  F(\omega) &= e^{-\frac{\sigma^2 \omega^2}{2}}
\end{align} $$

The Fourier transform is another Gaussian, but with inverse standard deviation $1/\sigma$.

This finding can be generalized to the **uncertainty relation**.
The more localized a signal in the time domain, the more broader in the frequency domain and vice versa.

> TODO: 2D FT

# 4. Windows and Resolution

In practice, signal analysis is always performed over limited time.
This can be modeled as a window function sliding across the signal.
Mathematically, the window function is multiplied with the signal, which mean a convolution in the frequency domain.

The shape of the window function determines the frequency domain resolution.
They are characterized by:

- Energy in the central peak compared to the total energy $\rightarrow$ The energy in the sidelobes will produce spectral artifacts
- The height of the first sidelobe compared to the central peak $\rightarrow$ The sidelobes may mask small spectral amplitudes near larger ones
- The half width (width at half amplitude) of the central peak $\rightarrow$ A broad peak will nearby frequencies

Some window functions:

- Boxcar: smallest half width, strongest sidelobes
- Kaiser-Bessel: broad half width, very weak sidelobes
- Hanning or Hamming: often good compromise

# 5. Discrete Fourier Transform

$$ \begin{align} 
F_k &= \frac{1}{N} \sum_{j=0}^{N-1} f(j e^{-i2\pi\frac{jk}{N}}) \\
f_j &= \sum_{k=0}{N-1} F_k e^{i2\pi\frac{jk}{N}}
\end{align} $$

$F_k$ are a spectrum, not a spectral density.

The kernel $W_k^{-jk} = e^{-2\pi\frac{jk}{N}}$ of the DFT is discrete and periodic in $N$.
This means the kernel has only $N$ values and each value is required $2N$ time in the sum.
In an inverse DFT, the kernel value are required in counter-clockwise order.

Since $n = jk$, the time and frequency domain indices are indistinguishable, which means the frequency series is also periodic in $N$.
Therefore, the upper half of the frequency series ($N/2..N-1$) contains no new information and is complex conjugate of the lower half.
The threshold is called the **Nyquist Frequency**.

$$ \begin{equation}
  f_{\text{nyq}} = \frac{f_s}{2} = \frac{1}{2 \deltat}
\end{equation} $$

$F_{N/2}$ is always real-valued, the corresponding $f_j$ at the Nyquist frequency is always even.
An odd signal at Nyquist cannot be respresented.

When the sample rate is below the Nyquist frequency, the orignal signal appears at a different frequency (their **alias**).
To avoid aliasing artifacts in signals, an analogue low-pass filter can be applied to remove frequencies above Nyquist.

It is possible to reconstruct the original continuous signal if the sampling was done correctly (unaliased) with sinc-interpolation.

> TODO: Fast Fourier transform

# 6. Discrete Time Fourier Transform

- Is the Fouier transform for aperiodic, discrete signals.
- In praxis used when waiting for the end of a data-stream is not an option

$$ \begin{align}
  F(\omega) &= \sum_{j=-\infty}^{\imfty} f_j e^{-i\omegaj\deltat} \\
  f_l &= \frac{1}{\omega_s} \int_{-\omega_s/2}^{\omega_s/2} F(\omega) e^{i\oemga l \delta t} d\omega
\end{align} $$

$F(\omega)$ is no longer a spectral density, just a spectrum, even though it is continuous.

The DTFT differs from the DFT by:

- Different boundary conditions, relevant for convolution and other operators
- A window function is required for never ending data-streams, which adds the window postition as a new dimension

# 8. Laplace Transform

The Laplace Transform is an extension of the Fourier transform.
It includes sinusoids and exponentials to represent a signal and allows a sparse description of a analogue signal in term of poles and zeros.

$$
\begin{align}
  F(s) &= \int_{-\infty}^\infty f(t) e^{-st} dt\\
  s &= \sigma + i\omega
\end{align}
$$

- $\sigma = 0$: the Laplace transform becomes a Fourier transform
- $\sigma > 0$: represents a damped signal.
Stabilizes the system for $t \rightarrow +\infty$ (causal part), destabilizes for $t \rightarrow + \infty$ (anti-causal part)
- Depending on the signal, the system can still be unstable in the causal part if $f(t)$ increases faster than the damping

**Inverse Laplace transform**

```math
  f_\sigma(t) = \frac{1}{2 \pi i} \int_{\sigma + i\omega}^{\sigma - i\omega} F(s) e^{st} ds
```

- The inverse Laplace transform is not unique. Different $\sigma$ may result in different signals.

**General transfer function**

```math
  F(s) = \frac{b_L \prod_{l=1}^L (s-z_l)}{a_M \prod_{m=1}{M} (s-p_m)}
```

- Each pole reduces the amplitude $\propto \omega^{-1}$, each zero amplifies it $\propto \omega^{-1}$
- Each pole shifts the phase -90deg, each zero +90deg

**Single Pole**

$$
\begin{align}
  F(s) &= \frac{1}{s-p}\\
  F(\omega) &= {1}{i\omega-p} = \frac{1}{r e^{i\phi}} = \frac{1}{r} e^{-i\phi}
\end{align}
$$

- The denominator can be interpreted as a vector pointing to the imaginary axis
- $\omega >> \omega_c$: the amplitude decays $A \propto \omega^{-1}$, the phase converges towards -90 deg

**Single Zero**

$$
\begin{align}
  F(s) &= s-z\\
  F(\omega) &= r e^{i\phi}
\end{align}
$$

- $\omega >> \omega_c$: the amplitude decays $A \propto \omega^{-1}$, the phase converges towards -90 deg

A stable, causal signal is:

- minimum phase, if all zeros are on the left s-plane
- maximum phase, if all zeros are on the right s-plane
- mixed phase, otherwise

Poles can be placed off the real axis:

- The closer to the imaginary axis, the larger the amplification
- A pole right on the imaginary axis creates a singularity at $\omega_c$.
The signal is unstable because the imaginary axis is not part of the ROC.
- For a signal to be real-valued, poles must lie on the real axis, or appear in complex conjugate pairs.

