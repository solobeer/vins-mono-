import cv2

image = cv2.imread("./fisheye_mask.jpg", flags=0)
hight = image.shape[0]
width = image.shape[1]
# chan = image.shape[2]
for h in range(hight):
    for w in range(width):
        if (image[h][w] != 0 and image[h][w] != 255) :
            if(image[h][w] < 200):
                image[h][w] = 0
            else:
                image[h][w] = 255
            print(image[h][w])
        if (h >= 450): 
            image[h][w] = 0
        

cv2.imwrite("./fisheye_mask_1.png", image)
  
# cv2.imshow("dst", image)

print(image)
print(image.shape)
# cv2.waitKey(0)
