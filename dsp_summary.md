# 2. Fourier Series

Any piecewise continuous, bounded and **periodic** function can be represented as a Fourier Series.

\begin{equation}
  f(t) = \sum_{k=0}^\infty \left( A_k \cos(k\omega_0t) + B_k \sin(k\omega_0t) \right)
\end{equation}

- sin and cos are orthogonal basis functions
- There is no information about frequencies between $k\omega_0$ and $(k+1)\omega_0$.
Therefore, $\omega_0$ is also the sampling interval.
The longer $T_0$, the smaller $\omega_0$ and the better the frequency resolution.

  TODO: Add coefficiants formulas

- An extra formula for $A_0$ is required, because of the factor 2.
- Fourier analysis: computing $A_k$ and $B_k$ from $f(t)$
- Fourier synthesis: computing $f(t)$ from $A_k$ and $B_k$
- When all $k$ are accounted for, analysis followed by synthesis is a no-op

  TODO: Time shift

- Kinks in the function require many $k$s for a good fit
- Steps require even more $k$s and lead to the Gibbs phenomenon:
There persists an overshoot, but the overshoot duration decreases.



# 8. Laplace Transform

The Laplace Transform is an extension of the Fourier transform.
It includes sinusoids and exponentials to represent a signal and allows a sparse description of a analogue signal in term of poles and zeros.

\begin{align}
  F(s) &= \int_{-\infty}^\infty f(t) e^{-st} dt\\
  s &= \sigma + i\omega
\end{align}

- $\sigma = 0$: the Laplace transform becomes a Fourier transform
- $\sigma > 0$: represents a damped signal.
Stabilizes the system for $t \rightarrow +\infty$ (causal part), destabilizes for $t \rightarrow + \infty$ (anti-causal part)
- Depending on the signal, the system can still be unstable in the causal part if $f(t)$ increases faster than the damping

**Inverse Laplace transform**

\begin{equation}
  f_\sigma(t) = \frac{1}{2 \pi i} \int_{\sigma + i\omega}^{\sigma - i\omega} F(s) e^{st} ds
\end{equation}

- The inverse Laplace transform is not unique. Different $\sigma$ may result in different signals.

**General transfer function**

\begin{equation}
  F(s) = \frac{b_L \prod_{l=1}^L (s-z_l)}{a_M \prod_{m=1}{M} (s-p_m)}
\end{equation}

- Each pole reduces the amplitude $\prop \omega^{-1}$, each zero amplifies it $\prop \omega^{-1}$
- Each pole shifts the phase -90deg, each zero +90deg

**Single Pole**

\begin{align}
  F(s) &= \frac{1}{s-p}\\
  F(\omega) &= {1}{i\omega-p} = \frac{1}{r e^{i\phi}} = \frac{1}{r} e^{-i\phi}
\end{align}

- The denominator can be interpreted as a vector pointing to the imaginary axis
- $\omega >> \omega_c$: the amplitude decays $A \prop \omega^{-1}$, the phase converges towards -90 deg

**Single Zero**

\begin{align}
  F(s) &= s-z\\
  F(\omega) &= r e^{i\phi}
\end{align}

- $\omega >> \omega_c$: the amplitude decays $A \prop \omega^{-1}$, the phase converges towards -90 deg

A stable, causal signal is:

- minimum phase, if all zeros are on the left s-plane
- maximum phase, if all zeros are on the right s-plane
- mixed phase, otherwise

Poles can be placed off the real axis:

- The closer to the imaginary axis, the larger the amplification
- A pole right on the imaginary axis creates a singularity at $\omega_c$.
The signal is unstable because the imaginary axis is not part of the ROC.
- For a signal to be real-valued, poles must lie on the real axis, or appear in complex conjugate pairs.

