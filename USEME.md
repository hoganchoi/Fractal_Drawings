# USE ME:
This is the USEME file. Here, I've documented how to run the program and interact with the 
text-based user interface.
### How to Install Necessary Packages:
This program uses packages such as NumPy, Matplotlib, etc, that may not be installed on your current
system. I've listed all the required packages that are needed to run this program on the `requirements.txt`
file. Please install all necessary packages from the text file using the code `pip install -r requirements.txt`
on your local machine or a Python virtual environment. After installing, you can now run the program through
the `__main__.py` function.
### How to Run and Navigate through Interface:
To run the program, type in the code `python __main__.py` into the terminal. You will be greeted with a message
that tells you to input the path to a folder you want to save your images in. Please note that you must use an
existing folder. If spelled incorrectly, the program may crash. 
After inputting a designated workspace folder, you will be met with 6 different choices. 
1. Create Fractal Canopy
2. Create Sierpinski Triangle
3. Create Koch Curve
4. Create Mandelbrot Fractal
5. Change ouptut directory
6. Exit Program
Please enter the corresponding number for a certain command. Below details the parameters you would need to input
for a certain Fractal.
#### Create Fractal Canopy:
When choosing this option, you will be directed to do the following:
- Please enter cutoff proportion (0 - 1) --Input the ratio of the next generated branch.
- Please enter branching angle --Signify the split angle between the branches.
- Please enter number of iterations (number of branches) --How many similar fractal shapes you want.
#### Create Sierpinski Triangle:
When choosing this option, you will be directed to do the following:
- Please enter the size of the triangle --How large do you want the triangle to be.
- Please enter the number of iterations (number of triangles) --How many similar fractal shapes you want.
#### Create Koch Curve:
When choosing this option, you will be directed to do the following:
- Please enter the number of iterations (number of curves) --How many Koch Curves you want.
#### Create Mandelbrot Fractal:
When choosing this option, you will be directed to do the following:
- Please enter the minimum x range --The minimum real number value.
- Please enter the maximum x range --The maximum real number value.
- Please enter the minimum y range --The minimum imaginary number value.
- Please enter the maximum y range --The maximum imaginary number value.
- Please enter the Mandelbrot cutoff threshold --The threshold of whether the given complex number is in the Mandelbrot Set.
- Please enter the number of iterations (number of testing) --How many times a complex number is iterated in the Mandelbrot equation.
- Please enter the resolution (number of pixels) --The number of points/pixels you want. 
- Please enter Y/N if you want scatter --If you choose scatter, it will plot points on the plot. However, if you don't use scatter, the Fractal will be colored in. Hence, not using scatter will result in a more defined structure.
### Notes:
As of right now, this program is very sensitive to errors. Hence, please make sure spellings and numbers are correct and makes sense. For example, please don't input a float number for number of iterations as it would most likely exit the program with an error. 
A write up for this program and the project is attached in this repository. There, I explain the mathematical properties of each fractal and how I coded them. There's also a folder named `fractal_drawings`. There are some drawings of fractals generated from this program (this could be a potential workspace).
Thank you very much for using the program!!!