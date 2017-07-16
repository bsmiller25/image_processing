import os
import sys
import time
import numpy as np
import scipy.ndimage as nd
import matplotlib.pyplot as plt
from scipy.ndimage.filters import median_filter as mf

# list the available images
path1 = "images"
path2 = "dot"
dpath = os.path.join(path1, path2)
flist = [os.path.join(dpath, i) for i in 
         sorted(os.listdir(os.path.join(dpath)))]

# read in the images as luminosity (averaging the color channels)
imgs = np.array([np.mean(nd.imread(i),axis = 2) for i in flist])

# generate temporally median filtered image set
imgs_filt = mf(imgs, [5,1,1])

# generate a background image by taking the average of the temporally filtered set
bg = np.mean(imgs_filt, axis = 0)

# create a foreground image set by subtracting the 
# background from the filterd original images
fgf = imgs_filt - bg

# create a foreground image set by subtracting the
# background from the original images 
fgo = imgs - bg

# plot the two differenced images
ysize = 4.
xsize = ysize*float(imgs[0].shape[1]) / float(imgs[0].shape[0])

fig, a = plt.subplots(1, 2, figsize = [2 * xsize, ysize])
a[0].axis("off")
a[1].axis("off")
a[0].set_title("Filtered BG")
a[1].set_title("Original BG")
im1 = a[0].imshow(abs(fgf[20]), cmap='gist_gray', clim=[0,50])
im2 = a[1].imshow(abs(fgo[20]), cmap='gist_gray', clim=[0,50])

fig.canvas.draw()
plt.show() 

