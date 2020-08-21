#Script to read and save image data.

import os

import cv2  # to read image
import numpy as np  # linear algebra
from PIL import Image  # for image processing

DATA = []  # fOR STORING IMAGES
LABELS = []  # fOR STORING LABELS
# Give a path where the dataset is located.
PARASITIZED = os.listdir("../content/cell_images/cell_images/Parasitized/")
UNINFECTED = os.listdir("../content/cell_images/cell_images/Uninfected/")

for i in PARASITIZED:
    try:
        image = cv2.imread("../content/cell_images/cell_images/Parasitized/" +
                           i)
        image_from_array = Image.fromarray(image, "RGB")
        size_image = image_from_array.resize((50, 50))
        DATA.append(np.array(size_image))
        LABELS.append(0)
    except AttributeError:
        pass

for u in UNINFECTED:
    try:
        image = cv2.imread("../content/cell_images/cell_images/Uninfected/" +
                           u)
        image_from_array = Image.fromarray(image, "RGB")
        size_image = image_from_array.resize((50, 50))
        DATA.append(np.array(size_image))
        LABELS.append(1)
    except AttributeError:
        pass
# DATA contains the RGB value of each image and
# LABELS is a list containing 0 or 1 based on whether it is parasitised or not.
CELLS = np.array(DATA)
LABELS = np.array(LABELS)

# Saving data as a numpy array.
np.save("Cells", CELLS)
np.save("Labels", LABELS)

# for loading saved data
CELLS = np.load("Cells.npy")
LABELS = np.load("labels.npy")
