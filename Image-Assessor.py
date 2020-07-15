#Image Manupilation
#Author: Osman Warsi
#Libraries: SimpleGraphics

# importing the library
from SimpleGraphics import *




## Handle the input
# @param: None  
# @return: the users choice
def InputHandler():
    userInput = int(input("Select one of the following: \n 1- Combine two whole images \n 2- blend horizontally \n 3- blend vertically \n"))
   #checking to see if userInput is out of range
    if userInput > 0 and userInput < 4:
        #returning the input
        return userInput
    else:
        #if input is out of range, call InputHandler again
        print("Invalid input, please try again:")
        #Recursive call
        InputHandler()

##  Blending the pixels of two images
# @param image1: first image
# @param image2: second image
# @param x: the x coordinate
# @param y: the y coordinate
# @return the RGB of final pixel (averaged out)
def blendPixel (image1, image2, x, y):

    #Retrieve r,g,b values
    r1, g1, b1 = getPixel(image1, x, y)
    r2, g2, b2 = getPixel(image2, x, y)

    #calculate average 
    rAvg = (r1 + r2)/2
    gAvg = (g1 + g2)/2
    bAvg = (b1 + b2)/2

    #Return the resulting blended pixel's RGB
    return rAvg, gAvg, bAvg

## To combine whole two images
# @param image1: first image
# @param image2: second image
# @return: resulting combined image
def combineAll(image1, image2):

    #loading the image
    img1 = loadImage(image1)
    img2 = loadImage(image2)
    #declaring height and width
    height = int(getHeight(img1))
    width = int(getWidth(img1))

    for x in range(0, width):
        for y in range(0, height):
            #Retrieve the pixels 
            r, g, b = blendPixel(img1, img2, x, y)
            #updating image1 in this case to be blended
            putPixel(img1, x, y, r, g, b)
    #Draw the resulting image
    drawImage(img1, 0, 0)

## Combine the images in parts (horizontally, and vertically)
# @param image1: the first image
# @param image2: the second image
# @param option: the choice to select which (horizontally or vertically)
# @return the appropriate combining method
def combineParts(image1, image2, option):
    img1 = loadImage(image1)
    img2 = loadImage(image2)
    height = int(getHeight(img1))
    width = int(getWidth(img1))
    
    
    #Declaring different splits in the image
    one = 0
    two = 150
    three = 250
    four = 400
    #Horizontal
    if option == 2:
        #Different splits defined
        split1=0
        split2= int(getHeight(img1)/3)
        split3= int(getHeight(img1)*0.6)
        split4=getHeight(img1)
        
        #Creating an empty image
        #ASSUMING images are 400 by 400
        horizontalImage = createImage(width  , height)
        #image on the top side
        for x in range(0, width):
            for y in range(0, split2):
                #get r, g, b
                r, g, b = getPixel(img1, x, y)
                putPixel(horizontalImage, x, y, r, g, b)
        #image on the bottom side
        for x in range(0,width):
            for y in range(split3, height ):
                #get r, g, b
                r, g, b = getPixel(img2, x, y)
                putPixel(horizontalImage, x, y, r, g, b)

        #middle combined area
        
        for x in range (0, getWidth(img1) ):
            for y in range(split2, split3):
                #Retrieve the pixels 
                r, g, b = blendPixel(img1, img2, x, y)
                putPixel(horizontalImage, x, y, r, g, b)
                #updating image1 in this case to be blended
        
            #Draw resulting image
            drawImage(horizontalImage, 0, 0)
            
            
    
    #Vertical
    if option == 3:
        #Different splits defined
        split1=0
        split2= int(getWidth(img1)/3)
        split3= int(getWidth(img1)*0.6)
        split4= int(getWidth(img1))
        
        verticalImage = createImage( height , split4)
        #image1 on left side
        for x in range(0, split2):
            for y in range(0, height):
                #get r, g, b
                r, g, b = getPixel(img1, x, y)
                putPixel(verticalImage, x, y, r, g, b)
        #image 2 on the right side
        for x in range(split3, height):
            for y in range(0, height):
                #get r, g, b
                r1, g1, b1 = getPixel(img2, x, y)
                putPixel(verticalImage, x, y, r1, g1, b1)
        
        #middle combined area
        for x in range (split2, split3):
            for y in range(0, height):
                #Retrieve the pixels 
                r, g, b = blendPixel(img1, img2, x, y)
                #updating image1 in this case to be blended
                putPixel(verticalImage, x, y, r, g, b)

        #Draw resulting image
        drawImage(verticalImage, 0, 0)

#MAIN 
choice = InputHandler()

if choice == 1:
    combineAll("image1.gif", "image2.gif")
elif choice == 2:
    combineParts("image1.gif", "image2.gif", 2)
elif choice == 3:
    combineParts("image1.gif", "image2.gif", 3)

#Defining the main window
resize(600, 800)
background("white")