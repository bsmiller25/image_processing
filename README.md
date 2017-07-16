# Image Processing Examples

image_manipulation.py
- Reads in an image
- Select every other pixel
- Swaps red and blue color values
- Converts to a negative image
- Applies a median filter
- Displays the new image

image_preview.py
- Allows interactive examination of images in the images directory
- Key bindings:
- - h:      plots a histogram of the R,G,B color channels
- - e:      plots a gaussian filtered view of the image
- - right:  next image
- - left:   last image
- - up:     skip ten images forward
- - down:   skip ten images back

regression_accuracy.py
- Uses regression for image recognition of hand-written digits

video_median_background.py
- Reads a bunch of images from the same vantage point
- Averages them to create a background image
- Filters the background image
- Creates foreground images using the original and filtered backgrounds
- Plot both foreground images for comparison

dot_scrape.py
- scrapes images from the NYC DOT live webcam site

Code written following examples and prompts from here: https://github.com/gdobler/atui_uc17

