from PIL import Image
import math




im = Image.open('dse-large.jpg') # Greyscale conversion
x = im.size[0]
y = im.size[1]
TotalPixels = x * y
pix = im.load()
PixelArray = [] 
SumForPicture = 0;
print(pix[1000,1000])

for i in range(x):
   for j in range(y):
      GreyscaleForPixel = (pix[i,j][0] + pix[i,j][1] + pix[i,j][2]) / 3 #Greyscale conversion
      #GreyscaleForPixel = pix[i,j]
      PixelArray.append(GreyscaleForPixel)
      SumForPicture += GreyscaleForPixel
      
MeanForPicture = SumForPicture / TotalPixels


SizeOfPixelArray = len(PixelArray)

print(SizeOfPixelArray)
print(TotalPixels)


SumOfTerms = 0
for i in range(SizeOfPixelArray):
    SumOfTerms += (PixelArray[i] - MeanForPicture) ** 2
    
Deviation = math.sqrt(SumOfTerms/SizeOfPixelArray)

print(Deviation*100/MeanForPicture)