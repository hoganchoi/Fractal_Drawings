## Import packages used in this class.
import os
import time
import numpy as np
import matplotlib.pyplot as plt
import warnings
warnings.filterwarnings("ignore")

## Represents a Mandelbrot Fractal class.
class MandelbrotSet():
  """
    A class that represents a Mandelbrot Fractal. When declared, users can 
    call functions with specific parameters to create a fractal.

    Attributes:
        xrange (tuple): The range of the real numbers.
        yrange (tuple): The range of the imaginary numbers.
        complex_set (np.array): An array full of complex numbers within the range of xrange and yrange.
        mandelbrot_set (np.array): An array full of complex numbers that satisfy Mandelbrot's condition.
        threshold (float): The cutoff threshold for Mandelbrot Set.
        num (int): The number of iterations of fractal.
        resolution (int): The number of pixels (complex numbers) generated.
        is_scatter (boolean): Whether the plot is scattered or binary.
        plot (pyplot): The plot where the fractal is drawn.
        ouptut_path (str): The output directory of where the drawing is stored.

    Methods:
        generate_complex_set(self): Generates an array of complex numbers within range.
        is_mandelbrot(self, c): Determines whether given complex number is in Mandelbrot Set.
        generate_mandelbrot_set(self): Returns an array full of complex numbers within Mandelbrot Set.
        draw_fractal(self): Draws and saves fractal using the parameters in class.

    Usage:
        This class is used to define and draw a Mandelbrot Fractal.
    """
  def __init__(self, xrange, yrange, threshold, num, resolution, scatter, output_path):
    """
    Initializes the Mandelbrot Fractal.

    Args:
        xrange (tuple): The range of the real numbers.
        yrange (tuple): The range of the imaginary numbers.
        threshold (float): The cutoff threshold for Mandelbrot Set.
        num (int): The number of iterations of fractal.
        resolution (int): The number of pixels (complex numbers) generated.
        is_scatter (boolean): Whether the plot is scattered or binary.
        ouptut_path (str): The output directory of where the drawing is stored.

    Returns:
        None
    """
    self.xrange = xrange
    self.yrange = yrange
    self.complex_set = None
    self.mandelbrot_set = None
    self.threshold = threshold
    self.num = num
    self.resolution = resolution
    self.is_scatter = scatter
    _, self.plot = plt.subplots()
    self.output_path = output_path
  
  def generate_complex_set(self):
    """
    Generates an array of complex numbers within range.

    Args:
        None

    Returns:
        None: Updates self.complex_set
    """
    xmin, xmax = self.xrange
    ymin, ymax = self.yrange
    real = np.linspace(xmin, xmax, int((xmax - xmin) * self.resolution))
    imag = np.linspace(ymin, ymax, int((ymax - ymin) * self.resolution))
    self.complex_set = real[np.newaxis, :] + (imag[:, np.newaxis] * 1j)

  def is_mandelbrot(self, c):
    """
    Returns if given complex number is within Mandelbrot Set.

    Args:
        c (complex): A given complex number within complex number set.

    Returns:
        (boolean): Whether complex number is within Mandelbrot Set.
    """
    z = 0
    for i in range(self.num):
      z = (z**2) + c
    return abs(z) <= self.threshold

  def generate_mandelbrot_set(self):
    """
    Returns an array full of complex numbers within Mandelbrot Set.

    Args:
        None

    Returns:
        mask (np.array): An array indicating which elements in complex set are Mandelbrot Set.
    """
    self.generate_complex_set()
    mask = self.is_mandelbrot(self.complex_set)
    self.mandelbrot_set = self.complex_set[mask]
    return mask

  def draw_fractal(self):
    """
    Draws and saves fractal given class.

    Args:
        None

    Returns:
        None
    """
    mask = self.generate_mandelbrot_set()
    if self.is_scatter is True:
      plt.scatter(self.mandelbrot_set.real, self.mandelbrot_set.imag, color="black", marker=",", s=1)
      self.plot.set_title(f'Mandelbrot Fractal with {self.resolution} Pixel Resolution')
      plt.gca().set_aspect("equal")
      self.plot.axis("off")
      timestamp = time.strftime("%Y%m%d%H%M%S")
      filename = "MandelbrotFractal_" + timestamp + ".png"
      final_output_path = os.path.join(self.output_path, filename)
      plt.savefig(final_output_path)
      plt.show()

    else:
      self.plot.imshow(mask, cmap = "binary")
      self.plot.set_title(f'Mandelbrot Fractal with {self.resolution} Pixel Resolution')
      plt.gca().set_aspect("equal")
      self.plot.axis("off")
      timestamp = time.strftime("%Y%m%d%H%M%S")
      filename = "MandelbrotFractal_" + timestamp + ".png"
      final_output_path = os.path.join(self.output_path, filename)
      plt.savefig(final_output_path)
      plt.show()
    