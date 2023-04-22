import cv2


name = 'img9.jpg'
img = cv2.imread(name)

print("Shape of the image", img.shape)

shape = img.shape
height = shape[0]
width = shape[1]
print(height,width)
c_height = int(height/5)

crop1 = img[:c_height,:width]
crop2 = img[c_height:c_height*2,:width]
crop3 = img[c_height*2:c_height*3,:width]
crop4 = img[c_height*3:c_height*4,:width]
crop5 = img[c_height*4:,:width]   

'''
cv2.imshow('original', img)
cv2.imshow('cropped1', crop1)
cv2.imshow('cropped2', crop2)
cv2.imshow('cropped3', crop3)
cv2.waitKey(0)
cv2.destroyAllWindows()
'''

im_v = cv2.vconcat([crop5,crop3,crop2,crop1])
cv2.imshow(name, im_v)
cv2.waitKey(0)
cv2.imwrite('img9jumbled.jpg',im_v)
cv2.destroyAllWindows()

