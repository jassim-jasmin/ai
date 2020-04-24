import numpy as np
import struct

with open('dataset/t10k-images.idx3-ubyte','rb') as f:
    magic, size = struct.unpack(">II", f.read(8))
    nrows, ncols = struct.unpack(">II", f.read(8))
    data = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
    data = data.reshape((size, nrows, ncols))



with open('dataset/t10k-labels.idx1-ubyte','rb') as f:
    magic, size = struct.unpack(">II", f.read(8))
    nrows, ncols = struct.unpack(">II", f.read(8))
    data_label = np.fromfile(f, dtype=np.dtype(np.uint8).newbyteorder('>'))
    # data_lable = data.reshape((size, nrows, ncols))

print(data_label[0])
import matplotlib.pyplot as plt
plt.imshow(data[0,:,:], cmap='gray')
plt.show()