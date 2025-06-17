import numpy as np
import matplotlib.pyplot as plt
import pywt

# Hard-coded signal data (8 samples)
signal = np.array([1, 2, 3, 4, 4, 3, 2, 1])
time_points = np.arange(len(signal))  # Create time axis

# Apply Wavelet Transform
wavelet = "db1"
coeffs = pywt.wavedec(signal, wavelet, level=2)
levels = len(coeffs)

# Create figure with subplots
plt.figure(figsize=(12, 8))

# Plot original signal
plt.subplot(levels + 1, 1, 1)
plt.plot(time_points, signal, "b-", linewidth=2)
plt.title("Original Signal")
plt.ylabel("Amplitude")
plt.grid(True)

# Plot approximation and detail coefficients
for i, coeff in enumerate(coeffs):
    plt.subplot(levels + 1, 1, i + 2)

    if i == 0:
        # Approximation coefficients
        plt.stem(np.arange(len(coeff)), coeff, "r", markerfmt="ro", basefmt=" ")
        plt.title(f"Approximation Coefficients (Level {i})")
    else:
        # Detail coefficients
        plt.stem(np.arange(len(coeff)), coeff, "g", markerfmt="go", basefmt=" ")
        plt.title(f"Detail Coefficients (Level {i})")

    plt.ylabel("Value")
    plt.grid(True)

plt.xlabel("Time (or Coefficient Index)")
plt.tight_layout()
plt.savefig("wavelet_transform.png", dpi=300)
plt.close()

# Print results
print("\nWavelet transform coefficients:")
for i, coeff in enumerate(coeffs):
    print(f"Level {i} coefficients: {coeff}")

print("\nPlot saved to wavelet_transform.png")


# Since we have a small hard-coded signal, we'll just print rather than plot

# import numpy as np
# import matplotlib.pyplot as plt
# from scipy.fft import fft, fftfreq

# # 1. Create a sample signal
# #    A sum of two sine waves with different frequencies and amplitudes
# #    Sampling rate
# sr = 1000
# # Sampling interval
# ts = 1.0/sr
# t = np.arange(0, 1, ts)

# freq1 = 5
# amp1 = 2
# signal1 = amp1 * np.sin(2 * np.pi * freq1 * t)

# freq2 = 50
# amp2 = 1
# signal2 = amp2 * np.sin(2 * np.pi * freq2 * t)

# signal = signal1 + signal2

# # 2. Apply Fourier Transform
# N = len(signal)
# yf = fft(signal)
# xf = fftfreq(N, ts)[:N//2] # Only consider the positive frequencies

# # 3. Visualize the original signal and its Fourier Transform
# plt.figure(figsize=(12, 6))

# plt.subplot(1, 2, 1)
# plt.plot(t, signal)
# plt.title('Original Signal (Time Domain)')
# plt.xlabel('Time (s)')
# plt.ylabel('Amplitude')
# plt.grid(True)

# plt.subplot(1, 2, 2)
# plt.plot(xf, 2.0/N * np.abs(yf[0:N//2])) # Plotting magnitude spectrum
# plt.title('Fourier Transform (Frequency Domain)')
# plt.xlabel('Frequency (Hz)')
# plt.ylabel('Magnitude')
# plt.grid(True)
# plt.tight_layout()
# plt.savefig('FT.png') # Saves the current figure as a PNG file

# print("Original signal length:", N)

# import numpy as np
# from umap import UMAP

# # Hard-coded data sample (4 samples with 5 features)
# X = np.array(
#     [
#         [1.2, 2.3, 3.1, 4.5, 5.0],
#         [0.9, 2.1, 2.9, 4.3, 4.8],
#         [1.1, 2.2, 3.0, 4.4, 4.9],
#         [1.3, 2.4, 3.2, 4.6, 5.1],
#     ]
# )

# # Apply UMAP with adjusted parameters for small dataset
# umap = UMAP(
#     n_components=2,
#     n_neighbors=2,  # Should be less than n_samples (4)
#     min_dist=0.1,  # Increased from default (0.1) for small dataset
#     random_state=42,
# )
# X_umap = umap.fit_transform(X)

# print("\nUMAP transformed data:")
# print(X_umap)


# import numpy as np
# from sklearn.decomposition import TruncatedSVD

# # Hard-coded data sample (4 samples with 5 features)
# X = np.array(
#     [
#         [1.2, 2.3, 3.1, 4.5, 5.0],
#         [0.9, 2.1, 2.9, 4.3, 4.8],
#         [1.1, 2.2, 3.0, 4.4, 4.9],
#         [1.3, 2.4, 3.2, 4.6, 5.1],
#     ]
# )

# # Hard-coded labels
# y = np.array([0, 1, 0, 1])

# # Apply SVD
# svd = TruncatedSVD(n_components=2)
# X_svd = svd.fit_transform(X)

# print("Hard-coded data sample:")
# print(X)
# print("\nSVD transformed data:")
# print(X_svd)
# print(f"\nExplained variance ratio: {svd.explained_variance_ratio_}")
