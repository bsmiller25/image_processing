import os
import sys
import numpy as np
import matplotlib.pyplot as plt
import scipy.ndimage as nd
import glob
from scipy.ndimage.filters import gaussian_filter as gf

def press(event):
    '''
    key bindings
    '''
    def close_extras():
        extras = plt.get_fignums()
        if len(extras) > 1:
            for e in extras[1:]:
                plt.close(e)
    
    # scroll right
    global spot
    global neg
    if event.key == "right":
        close_extras()
        spot = (spot + 1) % len(images)
        im.set_data(nd.imread(images[spot]))
        fig.canvas.draw()
        fig.canvas.set_window_title(images[spot])
        
    # scroll left    
    if event.key == "left":
        close_extras()
        spot = (spot - 1) % len(images)
        im.set_data(nd.imread(images[spot]))
        fig.canvas.draw()
        fig.canvas.set_window_title(images[spot])
        
    # scroll 10 right
    if event.key == "up":
        close_extras()
        spot = (spot + 10) % len(images)
        im.set_data(nd.imread(images[spot]))
        fig.canvas.draw()
        fig.canvas.set_window_title(images[spot])
    
    # scroll 10 left    
    if event.key == "down":
        close_extras()
        spot = (spot - 10) % len(images)
        im.set_data(nd.imread(images[spot]))
        fig.canvas.draw()
        fig.canvas.set_window_title(images[spot])
    
    # negative
    if event.key == "n":
        neg = ~neg
        if neg:
            im.set_data(255 - nd.imread(images[spot]))
        else:
            im.set_data(nd.imread(images[spot]))
        fig.canvas.draw()
        
    # absolute value of the gaussian derivative
    if event.key == "e":
        imgg = abs(gf(nd.imread(images[spot]), sigma=2))
        fig1, ax1 = plt.subplots(1, figsize=[xsize, ysize])
        fig1.subplots_adjust(0, 0, 1, 1)
        ax1.axis("off")
        im1 = ax1.imshow(imgg)
        fig1.canvas.set_window_title(images[spot])
        fig1.canvas.draw()
        plt.show()
        
    # histograms of colors
    if event.key == "h":
        img = nd.imread(images[spot])
        clrs = ["red", "green", "blue"]
        fig2, a = plt.subplots(1, 3, figsize = [3 * xsize, ysize])
        a = a.ravel()
        for i,axn in enumerate(a):
            axn.hist(img[:,:,i].flatten(), 
                     bins=255,
                     normed=True,
                     color=clrs[i],
                     range=[0, 255],
                     linewidth=0.0
                     )
        fig2.canvas.draw()
        plt.show() 



if __name__ == '__main__':
    # list all jpgs in directory
    path = "images"
    images = sorted(glob.glob(os.path.join(path,'*.jpg')))
    spot = 0
    neg = False
    
    # display image
    img = nd.imread(images[spot])
    ysize = 3.
    xsize = ysize*float(img.shape[1]) / float(img.shape[0])
    
    fig, ax = plt.subplots(1, figsize = [xsize, ysize])
    fig.subplots_adjust(0, 0, 1, 1)
    ax.axis("off")
    im = ax.imshow(img)
    fig.canvas.set_window_title(images[spot])
    fig.canvas.draw()
    
    # connect events
    fig.canvas.mpl_connect('key_press_event', press)
    
    plt.show()
