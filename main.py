import os
import numpy as np
import nibabel as nib
import matplotlib.pyplot as plt

# NOTICE: THIS ASSUMES YOU HAVE A FOLDER NAMED data WITH ALL THE .nii.gz FILES IN THE PROJECT DIRECTORY

# Loads the first image in the data folder
test_file = os.path.join('data', 'I004_1.nii.gz')
img = nib.load(test_file).get_fdata()

# Prints the x, y, and z dimensions of the img
# The img can be though of as a 3D arrangement of pixels, and we can examine slices of this 3D volume as 2D images
print(img.shape)

# Make a slice of the image on the z plane (Provides a top-down perspective I think)
test = img[:,:,20]

# Display the image
plt.imshow(test)
plt.show()
