import tkinter as tk
from tkinter import filedialog, messagebox

import cv2
import numpy as np
from keras.models import load_model

model = load_model("CNN.h5")

classes = {0: "Parasitized", 1: "Uninfected"}


def predict(
    path,
):  # Method for predicting whether the image is of parasitized cell or an uninfected cell
    img = cv2.imread(path)
    img = cv2.resize(img, (50, 50))
    img = img.reshape(-1, 50, 50, 3)
    img = img / 255.0
    prd = model.predict(img)
    certainty = np.amax(prd) * 100
    index = prd.argmax()  # Selecting Best Estimate
    messagebox.showinfo(
        "Result",
        "This cell is {} with {}% certainty.".format(classes[index], certainty),
    )


print("Please Enter The Image Of The Cell To Be Diagnosed: ", end="")

root = tk.Tk()
root.withdraw()
file_path = filedialog.askopenfilename()
predict(file_path)
