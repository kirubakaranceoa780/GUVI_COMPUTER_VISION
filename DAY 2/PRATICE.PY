import cv2
import matplotlib.pyplot as plt

img=cv2.imread("image.py")
h,w=img.shape[:2]
print(img.shape)
RM=cv2.getRotationMatrix2D((w//2,h//2),45,1.0)
rotated=cv2.warpAffine(img,RM,(w,h))
cv2.rectangle(img,(50,50),(100,100),(0,0,255),2)
cv2.circle(img,(20,30),40,(255,0,0),2)
plt.imshow(cv2.cvtColor(rotated,cv2.COLOR_BGR2RGB))
plt.axis("off")
plt.show()