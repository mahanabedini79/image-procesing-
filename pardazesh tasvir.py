import cv2 
import numpy as np 
import matplotlib.pyplot as plt 
img_template = cv2.imread("5shanbe.jpg",0)
img1 = cv2.imread("5shanbe.jpg",0)

orb = cv2.ORB_create()
kp1,des1 = orb.detectAndCompute(img_template,None)
kp2,des2 = orb.detectAndCompute(img1,None)

bf =cv2.BFMatcher(cv2.NORM_HAMMING , crossCheck =True)
matches = bf.match(des1, des2)  
matches = sorted(matches,key = lambda x:x.distance)
img_out = cv2.drawMatches(img1,kp2 , img_template , kp1,
                matches [:10000], None , flags=2)
plt.imshow(img_out)
plt.show()       
#algorithm_by_Mahan 

