import matplotlib.pyplot as plt
from netCDF4 import Dataset
import numpy as np

# step 1 ✅
# Open the NetCDF file
file_path = "ds/Sea Surface Temp.nc"
data = Dataset(file_path, "r")
# Display global attributes (metadata)
print("==== Global Attributes ====")
for attr in data.ncattrs():
    print(f"{attr}: {getattr(data, attr)}")

# Display variables and their shapes/dtypes
print("\n==== Variables ====")
for var_name in data.variables:
    var = data.variables[var_name]
    print(f"{var_name}:")
    print(f"  Dimensions: {var.dimensions}")
    print(f"  Shape: {var.shape}")
    print(f"  Data type: {var.dtype}")
    print(f"  Attributes: {var.__dict__}")

# Example: Check SST variable (adjust name if needed)
sst = data.variables["sst"][:]  # Replace 'sst' if the variable name differs
print(f"\nSST shape (time, lat, lon): {sst.shape}")

# step 2 ✅
# Check for missing values in SST
fill_value = (
    data.variables["sst"]._FillValue
    if "_FillValue" in data.variables["sst"].ncattrs()
    else None
)
print(f"Fill value for SST: {fill_value}")

# # Mask missing values (if they exist)
if fill_value is None:
    print("No missing values detected.")
else:
    sst = np.ma.masked_equal(sst, fill_value)
    print(f"Number of missing values: {np.sum(sst.mask)}")


# Extract coordinates (adjust names if needed)
lat = data.variables["lat"][:]
lon = data.variables["lon"][:]

# Plot a single time step (e.g., first time index)
time_idx = 0
sst_snapshot = sst[time_idx, :, :]

# step 3 ✅
# # Create contour plot
plt.figure(figsize=(10, 6))
contour = plt.contourf(lon, lat, sst_snapshot, levels=20, cmap="coolwarm")
plt.colorbar(contour, label="Sea Surface Temperature (°C)")

# # Add labels and title
plt.xlabel("Longitude")
plt.ylabel("Latitude")
plt.title(f"Sea Surface Temperature (Time Step {time_idx})")

plt.savefig("plots/conture.png")
