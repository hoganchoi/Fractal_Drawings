## Imports packages used in this class.
import os
import time
import numpy as np
import matplotlib.pyplot as plt

## Represents a Tree Fractal class.
class FractalCanopy():
  """
    A class that represents a Tree Fractal. When declared, users can 
    call functions with specific parameters to create a fractal.

    Attributes:
        x (float): The starting x-coordinate of the tree.
        y (float): The starting y-coordinate of the tree.
        length (float): The length of starting branch.
        angle (float): The starting angle of the branch.
        len_ratio (float): The cutoff ratio of the branch.
        rot_ang (float): The angle of the splitted branch.
        num (int): The number of iterations of fractal.
        plot (pyplot): The plot where the fractal is drawn.
        ouptut_path (str): The output directory of where the drawing is stored.

    Methods:
        find_x_end(self, x, length, angle): Finds the end of x-coordinate.
        find_y_end(self, y, length, angle): Finds the end of y-coordinate.
        create_fractal(self, x, y, length, angle, iter): Creates and plots fractal given parameters.
        draw_fractal(self): Draws and saves fractal using the parameters in class.

    Usage:
        This class is used to define and draw a Tree Fractal.
    """
  
  def __init__(self, len_ratio, rot_ang, num, output_path):
    """
    Initializes the Tree Fractal.

    Args:
        len_ratio (float): The cutoff ratio of the branch.
        rot_ang (float): The angle of the splitted branch.
        num (int): The number of iterations of fractal.
        ouptut_path (str): The output directory of where the drawing is stored.

    Returns:
        None
    """
    self.x = 0
    self.y = 0
    self.length = 10
    self.angle = 90
    self.len_ratio = len_ratio
    self.rot_ang = rot_ang
    self.num = num
    _, self.plot = plt.subplots()
    self.output_path = output_path

  def find_x_end(self, x, length, angle):
    """
    Returns the end of given x-coordinate.

    Args:
        x (float): The starting x-coordinate of the tree.
        length (float): The length of starting branch.
        angle (float): The starting angle of the branch.

    Returns:
        (float): The ending x-coordinate.
    """
    return (x + (length * np.cos(np.radians(angle))))

  def find_y_end(self, y, length, angle):
    """
    Returns the end of given y-coordinate.

    Args:
        y (float): The starting y-coordinate of the tree.
        length (float): The length of starting branch.
        angle (float): The starting angle of the branch.

    Returns:
        (float): The ending y-coordinate.
    """
    return (y + (length * np.sin(np.radians(angle))))

  def create_fractal(self, x, y, length, angle, iter):
    """
    Creates and plots fractal using arbitrary parameters.

    Args:
        x (float): The starting x-coordinate of the tree.
        y (float): The starting y-coordinate of the tree.
        length (float): The length of starting branch.
        angle (float): The starting angle of the branch.
        iter (int): The number of iterations of fractal.

    Returns:
        None: Updates self.plot.
    """
    if iter == 0:
      return None
    
    else:
      x_end = self.find_x_end(x, length, angle)
      y_end = self.find_y_end(y, length, angle)

      self.plot.plot([x, x_end], [y, y_end], color = 'black')

      self.create_fractal(x_end, y_end, length * self.len_ratio, angle + self.rot_ang, iter - 1)
      self.create_fractal(x_end, y_end, length * self.len_ratio, angle - self.rot_ang, iter - 1)

  def draw_fractal(self):
    """
    Draws and saves fractal given class.

    Args:
        None

    Returns:
        None
    """
    self.create_fractal(self.x, self.y, self.length, self.angle, self.num)
    self.plot.set_title(f'Fractal Canopy with {self.num} Iterations')
    self.plot.axis('off')
    timestamp = time.strftime("%Y%m%d%H%M%S")
    filename = "TreeCanopy_" + timestamp + ".png"
    final_output_path = os.path.join(self.output_path, filename)
    plt.savefig(final_output_path)
    plt.show()

    