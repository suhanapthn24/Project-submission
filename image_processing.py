import matplotlib.pyplot as plt
import matplotlib.image as mpimg

image = mpimg.imread('cat.jpg') 

plt.imshow(image)
plt.title('Cat')
plt.show()