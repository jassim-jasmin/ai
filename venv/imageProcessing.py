from scipy import misc
from PIL import Image
from libtiff import TIFF

test = Image.open('/root/Documents/mj/python/img.tif')
ascent = misc.ascent()
import matplotlib.pyplot as plt
plt.axis("off") # removes the axis and the ticks
plt.gray()
#plt.imshow(ascent)
plt.imshow(test)
# img_arr = plt.imread(test)
# plt.show()
tif = TIFF.open('/root/Documents/mj/python/img.tif', mode='r')
image = tif.read_image()
# l = image[:,:,:]
l = image
plt.imshow(l)
plt.show()
# for image in tif.iter_images():
#     print(image[0][0][0])