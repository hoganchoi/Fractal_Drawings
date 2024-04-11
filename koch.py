## Imports packages used in this class.
import os
import time
import numpy as np
import matplotlib.pyplot as plt

## Represents a Koch Curve class.
class KochCurve():
  """
    A class that represents a Koch Curve Fractal. When declared, users can 
    call functions with specific parameters to create a fractal.

    Attributes:
        coord1 (tuple): The starting coordinates of curve.
        coord2 (tuple): The ending coordinates of curve.
        num (int): The number of iterations of fractal.
        plot (pyplot): The plot where the fractal is drawn.
        ouptut_path (str): The output directory of where the drawing is stored.

    Methods:
        find_midpoint(self, coord1, coord2): Finds the midpoint given two coordinates (x or y).
        find_tri_point_beginning(self, coord1, coord2): Finds the beginning coordinates of triangle.
        find_tri_point_end(self, coord1, coord2): Finds the ending coordinates of triangle.
        find_tri_point_mid(self, coord1, coord2): Finds the coordinates of triangle's tip.
        create_fractal(self, x, y, length, angle, iter): Creates and plots fractal given parameters.
        draw_fractal(self): Draws and saves fractal using the parameters in class.

    Usage:
        This class is used to define and draw a Koch Curve Fractal.
    """
  
  def __init__(self, num, output_path):
    """
    Initializes the Koch Curve Fractal.

    Args:
        num (int): The number of iterations of fractal.
        ouptut_path (str): The output directory of where the drawing is stored.

    Returns:
        None
    """
    self.coord1 = (0, 0)
    self.coord2 = (10, 0)
    self.num = num
    _, self.plot = plt.subplots()
    self.output_path = output_path

  def find_midpoint(self, coord1, coord2):
    """
    Finds the midpoint given two coordinates (x or y).

    Args:
        coord1 (float): A given coordinate in either x or y value.
        coord2 (float): A given coordinate in either x or y value.

    Returns:
        (float): The mid point of given two coordinates.
    """
    return (coord1 + coord2) / 2

  def find_tri_point_beginning(self, coord1, coord2):
    """
    Finds the beginning coordinates of triangle.

    Args:
        coord1 (tuple): The starting coordinate of line segment.
        coord2 (tuple): The ending coordinate of line segment.

    Returns:
        (tuple): The starting coordinate in triangle.
    """
    coord_x = coord1[0] + ((coord2[0] - coord1[0]) / 3)
    coord_y = coord1[1] + ((coord2[1] - coord1[1]) / 3)
    return (coord_x, coord_y)

  def find_tri_point_end(self, coord1, coord2):
    """
    Finds the ending coordinates of triangle.

    Args:
        coord1 (tuple): The starting coordinate of line segment.
        coord2 (tuple): The ending coordinate of line segment.

    Returns:
        (tuple): The ending coordinate in triangle.
    """
    coord_x = coord1[0] + (2 * ((coord2[0] - coord1[0]) / 3))
    coord_y = coord1[1] + (2 * ((coord2[1] - coord1[1]) / 3))
    return (coord_x, coord_y)

  def find_tri_point_mid(self, coord1, coord2):
    """
    Finds the coordinates of triangle's tip.

    Args:
        coord1 (tuple): The starting coordinate of a given line segment.
        coord2 (tuple): The ending coordinate of a given line segment.

    Returns:
        (tuple): The coordinate of the created triangle.
    """
    coord_mid = ((coord1[0] + coord2[0]) / 2, (coord1[1] + coord2[1]) / 2)
    coord_x = coord_mid[0] + ((coord2[0] - coord1[0]) * np.cos(np.pi / 2)) - ((coord2[1] - coord1[1]) * np.sin(np.pi / 2))
    coord_y = coord_mid[1] + ((coord2[0] - coord1[0]) * np.sin(np.pi / 2)) + ((coord2[1] - coord1[1]) * np.cos(np.pi / 2))
    return (coord_x, coord_y)

  def create_fractal(self, coord1, coord2, iter):
    """
    Creates and plots fractal using arbitrary parameters.

    Args:
        coord1 (tuple): The starting coordinates of line segment.
        coord2 (tuple): The ending coordinates of line segment.
        iter (int): The number of iterations of fractal.

    Returns:
        None: Updates self.plot.
    """
    if iter == 0:
      self.plot.plot([coord1[0], coord2[0]], [coord1[1], coord2[1]], color = 'black')

    else:
      coord3 = self.find_tri_point_beginning(coord1, coord2)
      coord4 = self.find_tri_point_end(coord1, coord2)
      coord5 = self.find_tri_point_mid(coord3, coord4)

      self.create_fractal(coord1, coord3, iter - 1)
      self.create_fractal(coord3, coord5, iter - 1)
      self.create_fractal(coord5, coord4, iter - 1)
      self.create_fractal(coord4, coord2, iter - 1)

  def draw_fractal(self):
    """
    Draws and saves fractal given class.

    Args:
        None

    Returns:
        None
    """
    self.create_fractal(self.coord1, self.coord2, self.num)
    plt.gca().set_aspect("equal")
    self.plot.set_title(f'Koch Curve with {self.num} Iterations')
    self.plot.axis('off')
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = "KochCurve_" + timestamp + ".png"
    final_output_path = os.path.join(self.output_path, filename)
    plt.savefig(final_output_path)
    plt.show()