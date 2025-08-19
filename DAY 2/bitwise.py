import numpy as np
import matplotlib.pyplot as plt
import cv2
img=np.zeros((500,500),dtype=np.uint8)
circle=cv2.circle(img,(100,100),50,(255,0,0),-2)
plt.imshow(cv2.cvtColor(img,cv2.COLOR_BGR2RGB))
plt.show()
plt.axis("off")