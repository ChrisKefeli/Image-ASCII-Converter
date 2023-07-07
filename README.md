# Image-ASCII-Converter
  
### What does this do?

This is an image to ASCII converter program.
It will convert any image you give into ASCII format and paste it into a *.txt file in the same directory as the program.


## Prerequisites
In order to run the program, you'll need to have both the NumPy and Pillow libraries installed on your machine.
If you don't have the libraries installed, refer to below on how to install them:  

Windows: Open Command prompt  
Linux: Open terminal

Then type in:

```
pip install pillow
```

```
pip install numpy
```

If you're on Linux, type in `y` for yes when asked while installing the libraries.  

## Running the program
You can run it normally as you would with any other Python file.

#### IMPORTANT
__*Make sure you place the image you want to convert in the same directory as the ImageConverter.py file!*__

When running the program, you will be prompted to input the name of the image so no need to input the image name initially as an argument. See below for an example:
```py
python ImageConverter.py
Enter the name of the picture:
```
---
### To-do List
- [ ] Check if the file exists and prompt the user to ask again or quit

### Why did I make this?
Just a small project made in an afternoon. It provided an introduction to learning how to utilize external Python libraries like Pillow and NumPy to process simple data like from an image.
