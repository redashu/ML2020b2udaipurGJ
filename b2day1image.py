import  cv2  #  after  installing  opencv  
#  now  time  for  loading  image 
img=cv2.imread('dog.jpg')
#print(img)
#  now checking  type  data
print(type(img))
#  to check rows  and  col
print(img.shape)
#  croping  image
crimg=img[0:200,100:400]
#  to draw  something on image
#  line 
cv2.line(img,(0,0),(100,200),(0,0,255),10)
cv2.rectangle(img,(0,200),(100,400),(255,0,0),-1)
cv2.circle(img,(100,200),100,(0,255,0),-1)
#cv2.line(img,(50,100),(300,500),(120,160,200),10)
#      image data , first cord , sec cord , color , width
#  to show image
cv2.imshow('college',img)
#cv2.imshow('college1',crimg)
#          window name ,   image data 
#  apply  window hold down time
cv2.waitKey(0)   #  0 means  always open
