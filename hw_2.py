import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt

def markers_for_1(image):
    markers = np.zeros((image.shape[0],image.shape[1]),dtype ="int32")
    markers[90:140,90:140] = 255
    markers[236:255,0:20] = 1
    markers[0:20,0:20] = 1
    markers[0:20,50:70] = 1
    markers[5:10,130:150] = 1
    markers[0:20,236:255] = 1
    markers[236:255,236:255] = 1
    return markers

def markers_for_2(image):
    markers = np.zeros((image.shape[0],image.shape[1]),dtype ="int32")
    markers[90:140,90:140] = 255
    markers[30:70,150:200] = 255
    markers[70:100,240:245] = 255
    markers[70:100,245:255] = 1
    markers[50:70,245:255] = 1
    markers[236:255,0:20] = 1
    markers[0:20,0:20] = 1
    markers[0:10,50:200] = 1
    markers[230:240,60:100] = 1
    markers[0:20,236:255] = 1
    markers[236:255,236:255] = 1
    return markers

def markers_for_3(image):
    markers = np.zeros((image.shape[0],image.shape[1]),dtype ="int32")
    markers[90:140,90:140] = 255
    markers[236:255,0:20] = 1
    markers[0:20,0:20] = 1
    markers[0:20,236:255] = 1
    markers[100:155,240:255] = 1
    markers[210:215,105:110] = 255
    markers[236:255,236:255] = 1
    return markers

def markers_for_5(image):
    markers = np.zeros((image.shape[0],image.shape[1]),dtype ="int32")
    markers[70:150,50:150] = 255
    markers[80:100,205:210] = 255
    markers[236:255,0:20] = 1
    markers[0:20,0:20] = 1
    markers[75:90,20:25] = 1
    markers[200:255,40:50] = 1
    markers[0:20,236:255] = 1
    markers[236:255,236:255] = 1
    return markers

def markers_for_7(image):
    markers = np.zeros((image.shape[0],image.shape[1]),dtype ="int32")
    markers[90:140,90:140] = 255
    markers[236:255,0:20] = 1
    markers[0:20,0:20] = 1
    markers[0:20,50:70] = 1
    markers[150:170,210:220] = 1
    markers[65:75,240:250] = 1
    markers[236:255,236:255] = 1
    return markers

def markers_for_8(image):
    markers = np.zeros((image.shape[0],image.shape[1]),dtype ="int32")
    markers[90:140,90:140] = 255
    markers[236:255,0:20] = 1
    markers[50:60,40:50] = 1
    markers[0:20,0:20] = 1
    markers[0:20,236:255] = 1
    markers[236:255,236:255] = 1
    return markers

def CalcOfDamageAndNonDamage2(img_name, kernel_size):
    image = cv.imread(img_name)
    plt.imshow(image)
    plt.show()
    
    kernel = cv.getStructuringElement(cv.MORPH_ELLIPSE,(kernel_size,kernel_size))
    image_erode = cv.erode(image,kernel)
    plt.imshow(image_erode)
    plt.show()
    hsv_img1 = cv.cvtColor(image_erode,cv.COLOR_BGR2HSV)
    
    dst = cv.fastNlMeansDenoisingColored(image, None, kernel_size, kernel_size, 7, 21)
    plt.imshow(dst)
    plt.show()
    hsv_img2 = cv.cvtColor(dst,cv.COLOR_BGR2HSV)
    
    mst = cv.medianBlur(image, kernel_size)
    plt.imshow(mst)
    plt.show()
    hsv_img3 = cv.cvtColor(mst,cv.COLOR_BGR2HSV)
    
    if img_name == "_test/1.jpg":
        markers = markers_for_1(image)
    if img_name == "_test/2.jpg":
        markers = markers_for_2(image)
    if img_name == "_test/3.jpg":
        markers = markers_for_3(image)
    if img_name == "_test/5.jpg":
        markers = markers_for_5(image)
    if img_name == "_test/7.jpg":
        markers = markers_for_7(image)
    if img_name == "_test/8.jpg":
        markers = markers_for_8(image)
    
    leafs_area_BGR1 = cv.watershed(image_erode,markers)
    leafs_area_BGR2 = cv.watershed(dst,markers)
    leafs_area_BGR3 = cv.watershed(mst,markers)
    
    healthy_part1 = cv.inRange( hsv_img1,(36,25,25),( 86,255,255))
    ill_part1 = leafs_area_BGR1 - healthy_part1
    mask1 = np.zeros_like(image,np.uint8)
    mask1[leafs_area_BGR1 > 1] = (255,0,255)
    mask1[ill_part1 > 1] = (0,0,255)
    
    healthy_part2 = cv.inRange( hsv_img2,(36,25,25),( 86,255,255))
    ill_part2 = leafs_area_BGR2 - healthy_part2
    mask2 = np.zeros_like(image,np.uint8)
    mask2[leafs_area_BGR2 > 1] = (255,0,255)
    mask2[ill_part2 > 1] = (0,0,255)
    
    healthy_part3 = cv.inRange( hsv_img3,(36,25,25),( 86,255,255))
    ill_part3 = leafs_area_BGR3 - healthy_part3
    mask3 = np.zeros_like(image,np.uint8)
    mask3[leafs_area_BGR3 > 1] = (255,0,255)
    mask3[ill_part3 > 1] = (0,0,255)
    
    if img_name == "_test/1.jpg":
        cv.imwrite("_test/1_mod1.jpg",mask1)
        cv.imwrite("_test/1_mod2.jpg",mask2)
        cv.imwrite("_test/1_mod3.jpg",mask3)
    if img_name == "_test/2.jpg":
        cv.imwrite("_test/2_mod1.jpg",mask1)
        cv.imwrite("_test/2_mod2.jpg",mask2)
        cv.imwrite("_test/2_mod3.jpg",mask3)
    if img_name == "_test/3.jpg":
        cv.imwrite("_test/3_mod1.jpg",mask1)
        cv.imwrite("_test/3_mod2.jpg",mask2)
        cv.imwrite("_test/3_mod3.jpg",mask3)
    if img_name == "_test/5.jpg":
        cv.imwrite("_test/5_mod1.jpg",mask1)
        cv.imwrite("_test/5_mod2.jpg",mask2)
        cv.imwrite("_test/5_mod3.jpg",mask3)
    if img_name == "_test/7.jpg":
        cv.imwrite("_test/7_mod1.jpg",mask1)
        cv.imwrite("_test/7_mod2.jpg",mask2)
        cv.imwrite("_test/7_mod3.jpg",mask3)
    if img_name == "_test/8.jpg":
        cv.imwrite("_test/8_mod1.jpg",mask1)
        cv.imwrite("_test/8_mod2.jpg",mask2)
        cv.imwrite("_test/8_mod3.jpg",mask3)
        
    return (mask1,mask2,mask3)

tmp = CalcOfDamageAndNonDamage2("_test/1.jpg", 3)
plt.imshow(tmp[0])
plt.show()
plt.imshow(tmp[1])
plt.show()
plt.imshow(tmp[2])
plt.show()
tmp = CalcOfDamageAndNonDamage2("_test/2.jpg", 7)
plt.imshow(tmp[0])
plt.show()
plt.imshow(tmp[1])
plt.show()
plt.imshow(tmp[2])
plt.show()
tmp = CalcOfDamageAndNonDamage2("_test/3.jpg", 3)
plt.imshow(tmp[0])
plt.show()
plt.imshow(tmp[1])
plt.show()
plt.imshow(tmp[2])
plt.show()
tmp = CalcOfDamageAndNonDamage2("_test/5.jpg", 5)
plt.imshow(tmp[0])
plt.show()
plt.imshow(tmp[1])
plt.show()
plt.imshow(tmp[2])
plt.show()
tmp = CalcOfDamageAndNonDamage2("_test/7.jpg", 3)
plt.imshow(tmp[0])
plt.show()
plt.imshow(tmp[1])
plt.show()
plt.imshow(tmp[2])
plt.show()
tmp = CalcOfDamageAndNonDamage2("_test/8.jpg", 5)
plt.imshow(tmp[0])
plt.show()
plt.imshow(tmp[1])
plt.show()
plt.imshow(tmp[2])
plt.show()
k = cv.waitKey(0)
cv.destroyAllWindows()