import random
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

image_size = 28 # width and length
no_of_different_labels = 10 #  i.e. 0, 1, 2, 3, ..., 9
image_pixels = image_size * image_size
data_path = 'HW2/HW2_material/'
train_data = np.loadtxt('.\HW2\HW2_material\MNISTnumImages5000_balanced.txt', dtype=float)
train_labels = np.loadtxt('.\HW2\HW2_material\MNISTnumLabels5000_balanced.txt', dtype=float)

def img_extract(num_label):

    img = [train_data[key] for (key, label) in enumerate(train_labels) if int(label) == num_label]
    for i in range(500):
        image = img[i].reshape((28, 28))
        plt.subplot(20, 25, i + 1)
        plt.imshow(image, cmap="gray")
        plt.axis('off')
    # plt.tight_layout(pad=2.0)
    # plt.savefig(f'../assets/500_{num_label}figs.png')
    # plt.show()
    
def shuffle_lst(num_label):
    img = [train_data[key] for (key, label) in enumerate(train_labels) if int(label) == num_label]
    res = list()
    for i in range(400):
        res.append(img[i])
    return res

training_dataset = shuffle_lst(0) + shuffle_lst(1)
random.shuffle(training_dataset)


def make_dataset(num_label): 
    img = [train_data[key] for (key, label) in enumerate(train_labels) if int(label) == num_label]
    random.shuffle(img)
    res = list()
    for i in range(400, 500):
        res.append(img[i])
    return res


test_dataset = list()
challenge_dataset = list()

for i in range(10):
    if i == 0 or i == 1:
        test_dataset += make_dataset(i)
    elif i in [n for n in range(2, 10)]:
        challenge_dataset += make_dataset(i)
        
random.shuffle(test_dataset)
random.shuffle(challenge_dataset)
    
# if __name__ == '__main__':
#     for i in range(10):
#         if i == 0 or i == 1 or i == 7 or i == 9:
#             img_extract(i)