import numpy as np
import matplotlib as mpl
import matplotlib.pyplot as plt

def plot_image(instances, images_per_row=10, image_size = 32, **options):
    """Plot images of size IMAGE_SIZExIMAGE_SIZEx3

    Args:
        instances (list of numpy arrays): Each array is an image of size IMAGE_SIZExIMAGE_SIZEx3
        images_per_row (int, optional): Number of images per row. Defaults to 10.

    Reference: code is adopted from 
        Geron A: 2017, "Hands-On Machine Learning with Scikit-Learn and Tensorflow". 
    """

    images_per_row = min(len(instances), images_per_row)
    images = [instance for instance in instances]
    n_rows = (len(instances) - 1) // images_per_row + 1
    row_images = []
    n_empty = n_rows * images_per_row - len(instances)
    images.append(np.zeros((image_size, image_size * n_empty)))

    for row in range(n_rows):
        rimages = images[row * images_per_row: (row + 1) * images_per_row]
        row_images.append(np.concatenate(rimages, axis=1))

    image = np.concatenate(row_images, axis=0)
    plt.figure(figsize=(10,12))
    plt.imshow(image, cmap=mpl.cm.binary, **options)
    plt.axis("off")