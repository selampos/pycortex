import cortex
import numpy as np
import matplotlib.pyplot as plt

np.random.seed(1234)

subject = "S1"
xfm = "fullhead"

# Random data with one value per voxel
test_data = np.random.randn(31, 100, 100)

# Create pycortex volume
vol_data = cortex.Volume(
    test_data,
    subject,
    xfm,
    vmin=-2,
    vmax=2
)

# Display
cortex.quickshow(vol_data)
plt.show()

# Add 1
vol_plus = vol_data + 1
cortex.quickshow(vol_plus)
plt.show()

# Multiply by 4
vol_mult = vol_data * 4
cortex.quickshow(vol_mult)
plt.show()
