# TCL65R635Comparison

Grey uniformity seems to be the most visually obvious defect on TVs. You will often see reviews that 
talk about this same concept under the name “Dirty Screen Effect.” This effect varies on each TV from 
variations in assembly that cause pressures onto the LCD screen. People often refer to this as the 
“Panel Lottery”. The motivation behind this small project is to see how my TCL65R635 purchased from 
BestBuy on Black Friday 2021 objectively compares to RTING’s review to see if I’ve won the lottery:<br/>
https://www.rtings.com/tv/reviews/tcl/6-series-r635-2020-qled

## Overview:

I follow RTING’s test procedure for grey uniformity given the information at:<br/>
https://www.rtings.com/tv/tests/picture-quality/gray-uniformity-dirty-screen-effect-dse

The standard deviation output does not match that of RTING. I can’t be certain exactly how they went 
about their calculations but my program certainly gives an indication as to the severity of the grey 
uniformity but at a different scale than RTING.

The output of this application cannot be directly compared to RTINGs standard deviation percentages. To 
allow for a direct comparison I process various photos from past RTING tests regarding the grey uniformity 
through this application. Selecting TV models that vary throughout RTING’s 1-10 rating scale for grey 
uniformity will allow us to construct a mapping of my applications output to RTING’s 1-10 scale.  

I then take images of my store bought TCL65R635 using RTING’s 50% grey reference image (50%_Gray_Uniformity_RTING.png) 
projected onto the screen from a USB flash drive. I run the captured images through the StdDev-Gaussian.py application 
which performs a Gaussian filter and calculates a standard deviation output. 

I then determine a RTING’s 1-10 scale for my TCL65R635 using the constructed mapping. I can 
then objectively compare my TCL65R635 to RTING’s TCL65R635 review to see if I’ve won the lottery.

## Results:
The captured image from my TCL65R635 purchased from BestBuy of the 50% grey reference image outputs a 
standard deviation percentage of 4.192%. From the mapping we can see that this corresponds to a RTING 
rating of 7.5-7.6. 

The RTING’s TCL 6 Series/R635 2020’s 50% grey image capture outputs a 4.056% from my application and 
has a RTING score of 7.6.  I would say my TV having a 4.192% and a RTING score of 7.5-7.6 is very good. 

I’d say I won the lottery.

## Requirements:
- Python. I used Python 3.7.9 but most version of Python will work. 

- This application uses Pillow for image processing. To install use the following command on either Linux, 
Windows, or macOS:<br/>
`python -m pip install --upgrade pip`<br/>
`python -m pip install --upgrade Pillow`


## Image Capture:
RTING provide their camera settings used to capture the images used to calculate their standard deviation. 
Unfortunately I don’t have a camera capable of doing this. I used an IPhone Xs and captured the 50% grey 
reference image from my TV before the Iphone performed auto-exposure which blew out the image. I had 
slightly dim lighting conditions, not pitch black. After the image was taken I cropped it as close to the 
edges of the screen as I could.

My captured image is located under the name "TCLR635-BestBuy-BlackFriday2021.jpg"

## Mapping:
Grey uniformity test image captures were pulled from past TV model’s review pages and run though this application. 
The captured images provided by RTING have already gone through the Gaussian filter so I use the StdDev.py 
program instead which removes the Gaussian filter. StdDev.py and the images used for this mapping are located 
within Remap-RTING-Scoring. 

The following TVs were used and the following mapping was constructed:

| TV-Model  | Std.py Output  | RTING 50% grey uniformity 1-10 rating |
| :------------ |:---------------| :-----|
| [LG NANO90](https://www.rtings.com/tv/reviews/lg/nano90-2020)      | 12.545% | 5.6 |
| [Sony X750H](https://www.rtings.com/tv/reviews/sony/x750h)      | 10.842% | 6.4 |
| [Vizio V Series](https://www.rtings.com/tv/reviews/vizio/v-series-2020)      | 6.896% | 6.9 |
| [TCL 4 Series 2019](https://www.rtings.com/tv/reviews/tcl/4-series-2019)      | 5.257% | 7.4 |
| [TCL 4 Series 2020](https://www.rtings.com/tv/reviews/tcl/4-series-2020)      | 4.543% | 7.5 |
| [TCL 6 Series/R635](https://www.rtings.com/tv/reviews/tcl/6-series-r635-2020-qled)      | 4.056% | 7.6 |
| [Hisense U6G](https://www.rtings.com/tv/reviews/hisense/u6g)      | 3.522% | 8.0 |
| [Sony A9S OLED](https://www.rtings.com/tv/reviews/sony/a9s-oled)      | 1.993% | 8.4 |



