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

$$ \begin{align}
  A_0 &= \frac{1}{T_0} \oint f(t) dt \\
  B_0 &= 0\\
  A_k &= \frac{2}{T_0} \oint f(t) \cos(k \omega_0 t) dt\\
  B_k &= \frac{2}{T_0} \oint f(t) \sin(k \omega_0 t) dt\\
  F_k &= \frac{1}{T_0} \oint f(t) e^{-ik\omega_0t} dt
\end{align} $$

- An extra formula for $A_0$ is required, because of the factor 2.
- Fourier analysis: computing $A_k$ and $B_k$ from $f(t)$
- Fourier synthesis: computing $f(t)$ from $A_k$ and $B_k$
- When all $k$ are accounted for, analysis followed by synthesis is a no-op
- A time shifted signal has different phase but same amplitude spectrum
- Kinks in the function require many $k$s for a good fit
- Steps require even more $k$s and lead to the Gibbs phenomenon:
There persists an overshoot, but the overshoot duration decreases.

Conversion between coefficiants:

$$ \begin{align}
  a_0 &= \sqrt{A_0^2} = \sqrt{F_0 F_0*} \\
  a_k &= \sqrt{A_k^2 + B_k^2} = 2 \sqrt{F_k F_k^*} \\
  \phi_k &= \text{atan}\frac{B_k}{A_k} = - \text{atan}\frac{Im\{F_k\}}{Re\{F_k\}}
\end{align} $$ 

## Hermitian symmetry

$f(t)$ is real-valued:

- If $f(t) is even $\Rightarrow$ $F_k$ is even and and real ($B_k = 0$)
- If $f(t) is odd $\Rightarrow$ $F_k$ is odd and and imaginary ($A_k = 0$)

$f(t)$ is purely imaginary:

- If $f(t) is even $\Rightarrow$ $F_k$ is even and and imaginary ($A_k = 0$)
- If $f(t) is odd $\Rightarrow$ $F_k$ is odd and and real ($B_k = 0$)

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

## Convolution and Correlation

**Convolution** in time domain becomes multiplication in frequency domain:

$$ \begin{align}
  h(t) &= f(t) \star g(t) = \int_{-\infty}^\infty f(\tau) g(t - \tau) d\tau\\
  H(\omega) &= F(\omega) G(\omega)
\end{align} $$

**Correlation** is the same as convolution, but with flipping one signal.

- Convolution and correlation $\rightarrow$ identical amplitude spectra
- Deconvolution and correlation $\rightarrow$ identical phase spectra

## Plancherel's theorem

- relates the zero-lag correlation to the spectral densities

$$ \begin{equation}
  \int_{-\infty}^{\infty} f^\star(t) g(t) dt = \frac{1}{2 \pi} \int_{-\infty}^\infty F^\star(\omega) G(\omega) d\omega
\end{equation} $$

## Parseval's theorem

- Parcherel's theorem when $f=g$

$$ \begin{equation}
  \int_{-\infty}^\infty |f(t)|^2 dt = \frac{1}{2\pi} \int_{-\infty}^\infty |F(\omega)|^2 d\omega
\end{equation} $$

- $|f(t)|^2$ is the instantaneous power
- $|F(\omega)|^2$ is the Energy Spectral Denstiy (ESD)
- $|F_k|^2 would be called the Power Spectral Density (PSD)

$\Rightarrow$ The total energy of the signal is equal in the time and frequency domain (up to a constant).

## Dirac delta function

The Dirac delta function ($\Delta (t)$) can be used to pick a value at a specific time in an integral.
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

## Heaviside step function

The delta function is very important, but physically not realizeable (infinite amplitude).
The step function is a way around this.

$$ \begin{equation}
  FT\[u(t)\] = \frac{1}{i\omega} + \pi \delta(\omega)
\end{equation} $$

## Sign function

The sign function is not square integrable and cannot be Fourier transformed.
However, with a limit-process:

$$ \begin{equation}
  FT\[sgn(t)\] = \frac{2}{i\omega}
\end{equation} $$

## Boxcar function

$$ \begin{align}
  F(\kappa) &= T_0 \frac{\sin(\kappa)}{\kappa}\\
  \kappa &= \frac{\omega T_0}{2}
\end{align} $$

## Gaussian distribution

$$ \begin{align}
  f(t) &= \frac{1}{\sigma \sqrt{2\pi}} e^{-\frac{t^2}{2\sigma^2}}\\
  F(\omega) &= e^{-\frac{\sigma^2 \omega^2}{2}}
\end{align} $$

The Fourier transform is another Gaussian, but with inverse standard deviation $1/\sigma$.

This finding can be generalized to the **uncertainty relation**.
The more localized a signal in the time domain, the more broader in the frequency domain and vice versa.

## 2D Fourier Transform

- For example when seismic sensors are deployed along a line (time and position)
- The 2D integral can be seperated to 1D transforms $F(k_x, k_y) = FT_y\{FT_x\{f(x, y)\}\}$
- Rotating an image is quivalent to rotating in the 2D Fourier domain
- The spectral denstiy $F(f)$ on a signal traveling with constant velocity $c=f/k$ projects into a line with slope $c$

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

## Nyquist Frequency

Since $n = jk$, the time and frequency domain indices are indistinguishable, which means the frequency series is also periodic in $N$.
Therefore, the upper half of the frequency series ($N/2..N-1$) contains no new information and is complex conjugate of the lower half.
The threshold is called the **Nyquist Frequency**.

$$ \begin{equation}
  f_{\text{nyq}} = \frac{f_s}{2} = \frac{1}{2 \Delta t}
\end{equation} $$

$F_{N/2}$ is always real-valued, the corresponding $f_j$ at the Nyquist frequency is always even.
An odd signal at Nyquist cannot be respresented.

## Aliasing

When the sample rate is below the Nyquist frequency, the orignal signal appears at a different frequency (their **alias**).
To avoid aliasing artifacts in signals, an analogue low-pass filter can be applied to remove frequencies above Nyquist.

It is possible to reconstruct the original continuous signal if the sampling was done correctly (unaliased) with sinc-interpolation.

## Fast Fourier Transform

- Recursively split up a series of points in even and odd parts.
Each split halfes the computational work.
- The resulting algorithm is $O(n \text{log}(n))$ instead of $O(n^2)$

# 6. Discrete Time Fourier Transform

- Is the Fouier transform for aperiodic, discrete signals.
- In praxis used when waiting for the end of a data-stream is not an option

$$ \begin{align}
  F(\omega) &= \sum_{j=-\infty}^{\infty} f_j e^{-i\omega j\Delta t} \\
  f_l &= \frac{1}{\omega_s} \int_{-\omega_s/2}^{\omega_s/2} F(\omega) e^{i\omega l \delta t} d\omega
\end{align} $$

$F(\omega)$ is no longer a spectral density, just a spectrum, even though it is continuous.

The DTFT differs from the DFT by:

- Different boundary conditions, relevant for convolution and other operators
- A window function is required for never ending data-streams, which adds the window postition as a new dimension

# 7. LTI Filters

- LTI = linear time-invariant

$$ \begin{align}
  Y(\omega) &= H(\omega) X(\omega) \\
  y(t) &= (x \star h)(t)
\end{align} $$

$H(\omega)$ is called the **frequency response function** and $h(t)$ the **impulse response function**.
Ideally these response function would be found using a Dirac pulse and observing the result.
Practially it can be done using a step function, which is the differentiated.

## Finite Inpulse Response (FIR)
For a discrete aperiodic signal, the convolution becomes $y_i = \sum_{l=-\infty}^\infty h_l x_{i-l}$
If the filter only has a finite length of no-zero $h$ elements, we can write $y_i = \sum_{l=-L}^L h_l x_{i-l}$

## Inifinite Impulse Response (IIR)
The filter is no only a linear combination of the input but also the output.

$$ \begin{align}
  y_i &= \frac{1}{a_0} \left( \sum_{l=-L}^{L} b_l x_{i-l} - \sum_{m=-M; m\neq0}^{M} a_m y_{i-m} \right) \\
  Y(\omega) &= H(\omega) X(\omega) \\
  H(\omega) &= \frac{B(\omega)}{A(\omega)}
\end{align} $$

It feeds a past (or future) filter result back into the filter.
Therefore, it a memory, reaching back to infinity.
It needs to be expressed through recursion.
For certain $\omega_r$, it could happen that $A(\omega_r)=0$ and $X(\omega_r) \neq 0$, which leads to an unbounded output.
This means $A(\omega)$ needs to be chosed with caution.

Advantage:

- Can have steep flanks, which makes them computationally efficient

Disadvantage:

- Potentially unstable (Can produce unbounded output for bounded input)
- Accumulation of numerical inaccuracies

## Analogue filters

- For analogue filters, time domain convolution is impractical (can't store history)
- Instead, use derivatives to memorize the past (Taulor's theorem)

For analogue FIR filters:

$$ \begin{equation}
  H(\omega) = \sum_{l=-L}^L h_l (i\omega)^l
\end{equation} $$

For analogue IIR filters:

$$ \begin{equation}
  H(\omega) = \frac{B(\omega)}{A(\omega)} = \frac{\sum_{l=-L}^L b_l (i\omega)^l}{\sum_{m=-M}^M a_m (i\omega)^m}
\end{equation} $$

**Butterworth filter**: maximally steep slopes and maximally flat transfer in the passband.

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

