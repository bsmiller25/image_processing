import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
from scipy.ndimage.filters import median_filter as mf


# 1: read in and manipulate image
img = mf((255 - (nd.imread(os.path.join('images','city_image.jpg'))[::2][:,:,::-1])),[8,2,1]).clip(0,255).astype(np.uint8)

# 2: display it
ysize = 3.
xsize = ysize*float(img.shape[1]) / float(img.shape[0])

fig, ax = plt.subplots(1, figsize = [xsize, ysize])
fig.subplots_adjust(0, 0, 1, 1)
ax.axis("off")
im = ax.imshow(img)
fig.canvas.set_window_title('modified city image')
fig.canvas.draw()
plt.show()
