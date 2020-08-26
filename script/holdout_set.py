import os
import random
import shutil  # importing the required libraries

import cv2

PARASITE_DIR = r"..\..\cell_images\Parasitized"
UNINFECTED_DIR = r"..\..\cell_images\Uninfected"

TARGET_SIZE = (64, 64)
SAMPLES = 100


def create_test_set(
        parasite_dir=PARASITE_DIR,
        uninfected_dir=UNINFECTED_DIR,
        samples=SAMPLES,
        target_size=TARGET_SIZE,
):
    """
    Description:
    Python function to create a holdout dataset for final evaluation of our test model.
    Parameters:
    arg1 : path of the parasitic cells directory
    arg2 : path of the uninfected cells directory
    arg3 : number of samples to be transferred
    arg4 : shape of the image after resizing
    Return:
    A directory containing 200 images randomly sampled from the 2 classes (100 samples each).
    """

    # creating the directory for the holdout dataset images
    os.makedirs(r"..\holdout_dataset", exist_ok=True)
    target_dir = r"..\holdout_dataset"

    # iterating through the respective directories
    for directory in (parasite_dir, uninfected_dir):

        # iterating through a random sample of images from both the classes
        for path in random.sample(os.listdir(directory), samples):

            img_path = directory + "\\" + path

            # checking if the image path contains a file
            if os.path.isfile(img_path):
                # reading the image path and storing it
                img = cv2.imread(img_path)
                # open cv reads image in BGR format so converting it into RGB for further use
                img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
                # converting the images into the required size
                img = cv2.resize(img, target_size)
                # transferred the image from source dir to the target dir
                shutil.move(img_path, target_dir)

        print(
            f"Taken 100 samples from {directory} and shifted it to {target_dir}"
        )

    print("Total number of samples in the target directory is {}".format(
        len(os.listdir(r"..\holdout_dataset")))
          )  # printing the total number of images in holdout_dataset folder


create_test_set()
