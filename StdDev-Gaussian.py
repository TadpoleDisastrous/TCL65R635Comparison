from PIL import Image, ImageFilter
import math

# Each RGB pixel is converted to greyscale by taking the average of the three colors. 
# This is a quick method that is typically used. 
#
# We produce the Mean greyscale value to be used in the standard deviation formula from 
# the average of all the pixels that make up the image.
#
# We output the Mean percentage error.

  
image = Image.open('TCLR635-BestBuy-BlackFriday2021.jpg')
 
# Blurring on the cropped image to remove artifacts
# This is done by RTING so I follow the same procedure.
Gaussian_image = image.filter(ImageFilter.GaussianBlur)

x = Gaussian_image.size[0]
y = Gaussian_image.size[1]
TotalPixels = x * y
pix = Gaussian_image.load()
PixelArray = [] 
SumForPicture = 0;

for i in range(x):
   for j in range(y):
      GreyscaleForPixel = (pix[i,j][0] + pix[i,j][1] + pix[i,j][2]) / 3 #Greyscale conversion
      PixelArray.append(GreyscaleForPixel)
      SumForPicture += GreyscaleForPixel
      
MeanForPicture = SumForPicture / TotalPixels


SizeOfPixelArray = len(PixelArray)


SumOfTerms = 0
for i in range(SizeOfPixelArray):
    SumOfTerms += (PixelArray[i] - MeanForPicture) ** 2
    
Deviation = math.sqrt(SumOfTerms/SizeOfPixelArray)

print(Deviation*100/MeanForPicture)