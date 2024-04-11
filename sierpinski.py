## Imports packages used in this class.
import os
import time
import numpy as np
import matplotlib.pyplot as plt

## Represents a Sierpinski Triangle Fractal Class.
class SierpinskiTriangle:
    """
    A class that represents a Sierpinski Triangle Fractal. When declared, users can 
    call functions with specific parameters to create a fractal.

    Attributes:
        size (int): The overall size of the triangle.
        num (int): The number of iterations of fractal.
        coord1 (tuple): The first coordinate of the triangle.
        coord2 (tuple): The second coordinate of the triangle.
        coord3 (tuple): The third coordinate of the triangle.
        plot (pyplot): The plot where the fractal is drawn.
        ouptut_path (str): The output directory of where the drawing is stored.

    Methods:
        find_midpoint(self, coord1, coord2): Finds the midpoint of two given coordinates.
        create_fractal(self, x, y, length, angle, iter): Creates and plots fractal given parameters.
        draw_fractal(self): Draws and saves fractal using the parameters in class.

    Usage:
        This class is used to define and draw a Sierpinski's Triangle Fractal.
    """
    
    def __init__(self, size, num, output_path):
        """
        Initializes the Tree Fractal.

        Args:
            size (int): The overall size of the triangle.
            num (int): The number of iterations of fractal.
            ouptut_path (str): The output directory of where the drawing is stored.

        Returns:
            None
        """
        self.size = size
        self.num = num
        self.coord1 = (0, 0)
        self.coord2 = (self.size, 0)
        self.coord3 = (self.size / 2, (self.size * np.sqrt(3)) / 2)
        _, self.plot = plt.subplots()
        self.output_path = output_path

    def find_midpoint(self, coord1, coord2):
        """
        Finds the midpoint of two given coordinates.

        Args:
            coord1 (tuple): The first given coordinate.
            coord2 (tuple): The second given coordinate.

        Returns:
            (tuple): The coordinate at the midpoint.
        """
        return ((coord1[0] + coord2[0]) / 2, (coord1[1] + coord2[1]) / 2)
    
    def create_fractal(self, coord1, coord2, coord3, iter):
        """
        Creates and plots fractal using arbitrary parameters.

        Args:
            coord1 (tuple): The first coordinate in triangle.
            coord2 (tuple): The second coordinate in triangle.
            coord3 (tuple): The third coordinate in triangle.
            iter (int): The number of iterations of fractal.

        Returns:
            None: Updates self.plot.
        """
        if iter == 0:
            self.plot.fill([coord1[0], coord2[0], coord3[0], coord1[0]], [coord1[1], coord2[1], coord3[1], coord1[1]], color = 'black')
        else:
            midpoint1 = self.find_midpoint(coord1, coord2)
            midpoint2 = self.find_midpoint(coord2, coord3)
            midpoint3 = self.find_midpoint(coord1, coord3)

            self.create_fractal(coord1, midpoint1, midpoint3, iter - 1)
            self.create_fractal(midpoint1, coord2, midpoint2, iter - 1)
            self.create_fractal(midpoint3, midpoint2, coord3, iter - 1)

    def draw_fractal(self):
        """
        Draws and saves fractal given class.

        Args:
            None

        Returns:
            None
        """
        self.create_fractal(self.coord1, self.coord2, self.coord3, self.num)
        self.plot.set_title(f'Sierpinski Triangle with {self.num} Iterations')
        self.plot.axis('off')
        timestamp = time.strftime("%Y%m%d%H%M%S")
        filename = "SierpinskiTriange_" + timestamp + ".png"
        final_output_path = os.path.join(self.output_path, filename)
        plt.savefig(final_output_path)
        plt.show()