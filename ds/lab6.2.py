import numpy as np
import matplotlib.pyplot as plt
from scipy.fft import fft, fftfreq
import pywt

# 1. Create sample signal
def create_signal(t):
    """Generate composite signal with multiple frequencies and a spike"""
    signal = (1.0 * np.sin(2 * np.pi * 5 * t) +  # Low frequency
              0.5 * np.sin(2 * np.pi * 20 * t) + # Medium frequency
              0.3 * np.sin(2 * np.pi * 50 * t) + # High frequency
              2.0 * (t == 0.5))                  # Spike at 0.5 seconds
    return signal

# Time parameters
t_max = 1.0                # Signal duration (seconds)
n_points = 1000            # Number of data points
t = np.linspace(0, t_max, n_points)  # Time vector
signal = create_signal(t)  # Generate signal

# 2. Fourier Transform
fft_result = fft(signal)                   # Compute FFT
freqs = fftfreq(n_points, t_max/n_points)  # Frequency bins
magnitude = np.abs(fft_result)             # Magnitude spectrum

# 3. Wavelet Transform (Continuous Wavelet Transform)
scales = np.arange(1, 128)                 # Wavelet scales
coef, freqs_wavelet = pywt.cwt(signal, scales, 'morl')  # Morlet wavelet
power = np.abs(coef)**2                    # Power spectrum

# 4. Visualization
plt.figure(figsize=(15, 10))

# Original signal
plt.subplot(3, 1, 1)
plt.plot(t, signal, 'b')
plt.title('Original Signal')
plt.xlabel('Time (s)')
plt.ylabel('Amplitude')
plt.grid(alpha=0.3)

# Fourier Transform
plt.subplot(3, 1, 2)
plt.plot(freqs[:n_points//2], magnitude[:n_points//2], 'r')
plt.title('Fourier Transform (Frequency Domain)')
plt.xlabel('Frequency (Hz)')
plt.ylabel('Magnitude')
plt.xlim(0, 100)  # Zoom to relevant frequencies
plt.grid(alpha=0.3)

# Wavelet Transform
plt.subplot(3, 1, 3)
plt.contourf(t, scales, power, 100, cmap='viridis')
plt.title('Wavelet Transform (Time-Frequency Domain)')
plt.xlabel('Time (s)')
plt.ylabel('Scale')
plt.colorbar(label='Power')
plt.tight_layout()
plt.show()