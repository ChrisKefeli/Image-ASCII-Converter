import numpy as np
from PIL import Image

#Promt the user to enter a file name
search = input("Enter the name of the picture: ")

#Ramp for the GreyScale conversion
ramp = ' $@B%8&WM#*oahkbdpqwmZO0QLCJUYXzcvunxrjft/\|()1{}[]?-_+~i!lI;:,\"^`". '

## Method to conect an image to greyscale 
# @param img
# @return image, this image was converted to greyscale
def ConvertToGrey(img):
    image = Image.open(img).convert('L')
    return image
    
## Method to convert the image to ASCII format
# @param image
# @param ramp
# @return string, Returns the string containing the image that was converted to ASCII     
def image_to_ascii(image, ramp):
    pixels = np.array(image)
    ascii_image = ''
    for row in pixels:
        for pixel in row:
            ascii_char = ramp[pixel // 32]
            ascii_image += ascii_char
        ascii_image += '\n'
    return ascii_image

# Convert the image to grey
gray_image = ConvertToGrey(search)

# Resize the image so it looks better in the .txt file
width, height = gray_image.size    
ratio = height / width / 2
new_width = 300
new_height = int(new_width * ratio)
smaller_image = gray_image.resize((new_width, new_height))

# Run the function 
ascii_image = image_to_ascii(smaller_image, ramp)

# Open the .txt file and write the ASCII text to the file
with open("Image.txt", "w+") as f:
    f.write(ascii_image)

print("Finished")
