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

    hsv_img = cv.cvtColor(image_erode,cv.COLOR_BGR2HSV)
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
    
    leafs_area_BGR = cv.watershed(image_erode,markers)
    healthy_part = cv.inRange( hsv_img,(36,25,25),( 86,255,255))
    ill_part = leafs_area_BGR - healthy_part
    mask = np.zeros_like(image,np.uint8)
    mask[leafs_area_BGR > 1] = (255,0,255)
    mask[ill_part > 1] = (0,0,255)
    return mask

plt.imshow(CalcOfDamageAndNonDamage2("_test/1.jpg", 3))
plt.show()
plt.imshow(CalcOfDamageAndNonDamage2("_test/2.jpg", 7))
plt.show()
plt.imshow(CalcOfDamageAndNonDamage2("_test/3.jpg", 3))
plt.show()
plt.imshow(CalcOfDamageAndNonDamage2("_test/5.jpg", 5))
plt.show()
plt.imshow(CalcOfDamageAndNonDamage2("_test/7.jpg", 3))
plt.show()
plt.imshow(CalcOfDamageAndNonDamage2("_test/8.jpg", 5))
plt.show()
k = cv.waitKey(0)
cv.destroyAllWindows()