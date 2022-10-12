import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = 'HW2/HW2_material/'
train_data = np.loadtxt('.\HW2\HW2_material\MNISTnumImages5000_balanced.txt', dtype=float)

fac = 0.99 / 255 # to avoid 0
train_imgs = np.asfarray(train_data[1:]) * fac + 0.01
train_labels = np.asfarray(train_data[:, :1])

for i in range(10):
    img = train_imgs[i].reshape((28,28))
    plt.imshow(img, cmap="Greys")
    plt.show()