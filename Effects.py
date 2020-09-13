import numpy as np
import cv2
from scipy.interpolate import UnivariateSpline

temp_image=None
temp_out=None
prev_amount=None

def clearTemp():
    global temp_image
    temp_image=None
    temp_out=None
    prev_amount=None

def sepia(image,amount):
    global temp_image,temp_out
    if np.all(temp_image!=image):
        temp_image=image
        kernel = np.array([[0.272, 0.534, 0.131],
                        [0.349, 0.686, 0.168],
                        [0.393, 0.769, 0.189]])
        sepia=cv2.transform(image,kernel)
        temp_out=sepia
    amount=amount/100
    return cv2.addWeighted(image,1-amount,temp_out,amount,0)

def brightness(image, amount):
    return cv2.convertScaleAbs(image,beta=amount)

def saturation(image, amount):
    hsv=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    hsv[:,:,1]=cv2.convertScaleAbs(hsv[:,:,1],beta=amount)
    return cv2.cvtColor(hsv, cv2.COLOR_HSV2BGR)

def sharpness(image, amount):
    global temp_image,temp_out
    if np.all(temp_image!=image):
        temp_image=image
        kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
        res=cv2.filter2D(image,-1,kernel)
        temp_out=res
    amount=amount/100
    return cv2.addWeighted(image, 1-amount, temp_out, amount, 0)

def warm(image, amount):
    x,y1=[0, 64, 128, 256], [0, 80, 160, 256]
    spline=UnivariateSpline(x,y1)
    np.set_printoptions(suppress=True)
    inc_lut=spline(range(256))
    x,y2=[0, 64, 128, 256], [0, 50, 100, 256]
    spline=UnivariateSpline(x,y2)
    dec_lut=spline(range(256))
    image2=image.copy()
    b, g, r = cv2.split(image)
    b=np.uint8(cv2.LUT(b,dec_lut))
    r=np.uint8(cv2.LUT(r, inc_lut))
    image2=cv2.merge((b,g,r))
    amount=amount/100
    return cv2.addWeighted(image, 1-amount, image2, amount, 0)
    
def cold(image, amount):
    x,y1=[0, 64, 128, 256], [0, 80, 160, 256]
    spline=UnivariateSpline(x,y1)
    np.set_printoptions(suppress=True)
    inc_lut=spline(range(256))
    x,y2=[0, 64, 128, 256], [0, 50, 100, 256]
    spline=UnivariateSpline(x,y2)
    dec_lut=spline(range(256))
    image2=image.copy()
    b, g, r = cv2.split(image)
    r=np.uint8(cv2.LUT(r,dec_lut))
    b=np.uint8(cv2.LUT(b, inc_lut))
    image2=cv2.merge((b,g,r))
    amount=amount/100
    return cv2.addWeighted(image, 1-amount, image2, amount, 0)

def equalise(image, amount):
    b , g, r = cv2.split(image)
    b_eql = cv2.equalizeHist(b)
    g_eql = cv2.equalizeHist(g)
    r_eql = cv2.equalizeHist(r)
    image2=cv2.merge((b_eql, g_eql, r_eql))
    amount=amount/100
    return cv2.addWeighted(image, 1-amount , image2, amount, 0)

def cartoon(image, amount):
    grey=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    blf=cv2.bilateralFilter(image, 5, 250, 250)
    medblur=cv2.medianBlur(grey, 5)
    amount=int(amount/10)
    if amount<=1:
        amount=3
    amount=amount if amount%2==1 else amount+1
    adap=cv2.adaptiveThreshold(medblur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, amount, 2)
    adap=cv2.cvtColor(adap, cv2.COLOR_GRAY2BGR)
    image2=cv2.bitwise_and(blf,adap)
    return image2

def blurring(image, amount):
    amount=int(amount//10)
    if amount==1:
        amount=3
    amount=amount+1 if amount%2==0 else amount
    return cv2.blur(image, (amount, amount))

def pencil_sketch(image, amount):
    grey=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    medblur=cv2.medianBlur(grey, 5)
    amount=int(amount/10)
    if amount<=1:
        amount=3
    amount=amount if amount%2==1 else amount+1
    adap=cv2.adaptiveThreshold(medblur, 255, cv2.ADAPTIVE_THRESH_GAUSSIAN_C, cv2.THRESH_BINARY, amount, 2)
    return adap

def noise_reduction(image, amount):
    global temp_image
    if np.all(temp_image!=image):
        temp_image=image
        temp_image=cv2.fastNlMeansDenoisingColored(image, None , 7, 31, 51 , 10)
    amount=amount/100
    return cv2.addWeighted(image,1-amount,temp_image,amount,0)

def negative(image, amount):
    image2=cv2.bitwise_not(image)
    amount=amount/100
    return cv2.addWeighted(image, 1-amount, image2, amount, 0 )

def redden(image, amount):
    image[:, :, 2]=cv2.convertScaleAbs(image[:, :, 2], beta=amount)
    return image
def greenify(image, amount):
    image[:, :, 1]=cv2.convertScaleAbs(image[:, :, 1], beta=amount)
    return image
def nili_panni(image, amount):
    image[:, :, 0]=cv2.convertScaleAbs(image[:, :, 0], beta=amount)
    return image

def yellow_panni(image, amount):
    image[:, :, 1]=cv2.convertScaleAbs(image[:, :, 1], beta=amount)
    image[:, :, 2]=cv2.convertScaleAbs(image[:, :, 2], beta=amount)
    return image

def vignette(image, amount):
    global prev_amount, temp_out
    if amount==prev_amount:
        return temp_out
    prev_amount=amount
    rows, cols=image.shape[:2]
    amount=255*2-(amount*255*2/100)
    image=np.float64(image)/255
    gauss_x=cv2.getGaussianKernel(cols, sigma= 90+amount).reshape([1, -1])
    gauss_y=cv2.getGaussianKernel(rows , sigma= 90+amount).reshape([-1, 1])
    kernel=gauss_x*gauss_y
    kernel=kernel/kernel.max()
    kernel=np.expand_dims(kernel, axis=2)
    image=np.uint8(image*kernel*255)
    temp_out=image.copy()
    return image

def emboss(image, amount):
    global temp_image
    global temp_out
    gray_image=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
    if np.all(temp_image!=image):
        temp_image=image.copy() 
        h , w= image.shape[:2]     
        y= np.ones((h, w), dtype=np.float32)*128
        output_mat=np.zeros((h, w), dtype=np.float32)
    
        kernel_topleft=np.array([[1, 1, 0], [1 , 0 , -1], [0 , -1 , -1]]).astype(np.float32)
        kernel_topright=np.array([[0, 1 , 1], [-1 , 0 , 1], [-1, -1, 0]]).astype(np.float32)
        temp1=np.float32(cv2.filter2D(gray_image, -1, kernel_topleft))
        temp2=np.float32(cv2.filter2D(gray_image, -1, kernel_topright))
        for i in range(h):
            for j in range(w):
                output_mat[i, j] = max(temp1[i, j], temp2[i, j])
        temp_out=np.uint8(cv2.add(output_mat, y))
    amount=amount/100
    return cv2.addWeighted(gray_image, 1-amount, temp_out, amount, 0)

def hdr(image, amount):
    image=cv2.cvtColor(image, cv2.COLOR_BGR2HSV)
    image[:, :, 1]=cv2.convertScaleAbs(image[:, :, 1], beta=int((amount/10))) 
    image=cv2.cvtColor(image, cv2.COLOR_HSV2BGR)
    image=cv2.convertScaleAbs(image, beta=amount//10)
    kernel=np.array([[0,-1,0],[-1,5,-1],[0,-1,0]])
    amount=amount/100
    res=cv2.filter2D(image,-1,kernel)
    
    return cv2.addWeighted(image, 1-amount, res, amount, 0)
