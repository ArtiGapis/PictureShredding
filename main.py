import matplotlib.pyplot as plt
import matplotlib as mpl
from scipy import misc
import numpy as np

mpl.use('TkAgg')  # !IMPORTANT
org_img = misc.face()


def shredder(img):
    first_pic_array = np.empty((0,), dtype=float)
    second_pic_array = np.empty((0,), dtype=float)
    pic_child_array = np.arange(64, dtype=object).reshape(8, 8)
    pic_array = np.split(img, 8)
    pic_array = np.array(pic_array)

    for n in range(8):
        pic_child_array[n] = np.split(pic_array[n], 8)

    for i in pic_child_array:
        first_pic_array = np.append(first_pic_array, i[::2])
        second_pic_array = np.append(second_pic_array, i[1::2])

    first_pic = np.concatenate(first_pic_array, axis=0)
    second_pic = np.concatenate(second_pic_array, axis=0)

    return np.concatenate((first_pic, second_pic))


partial_pic = shredder(org_img)

final_pic = np.rot90(shredder(np.rot90(partial_pic)), k=1, axes=(1, 0))

fig, axes, = plt.subplots(nrows=1, ncols=3, figsize=(10, 5))
axes[0].imshow(org_img, cmap='gray')
axes[0].set_title('Original image')
axes[1].imshow(partial_pic, cmap='gray')
axes[1].set_title('Partial image')
axes[2].imshow(final_pic, cmap='gray')
axes[2].set_title('Final image')
plt.show()
