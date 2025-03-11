# Converte uma imagem para grayscale e exporta TXT

from PIL import Image
import numpy as np

img = Image.open('imgs/UNIFOR_logo.png')
img = img.convert('L')

arr = np.asarray(img)
np.savetxt('data/UNIFOR_sample.txt', arr, fmt='%d')

img.save('imgs/UNIFOR_sample.png')
img.show()