## Import packages used in this class.
from canopy import FractalCanopy
from sierpinski import SierpinskiTriangle
from koch import KochCurve
from mandelbrot import MandelbrotSet

## Represents the console interface user's will interact with.
class FractalConsole():
    """
    A class that represents the text console that user's will interact with when creating
    and drawing fractals.

    Attributes:
        fractal (class): One of the four Fractal Classes.
        ouptut_path (str): The output directory of where the drawing is stored.
        is_running (boolean): Whether or not the system is currently running.

    Methods:
        run_program (self): Runs the text console.

    Usage:
        This class is used to define the text based console for Fractal Generation.
    """
    
    def __init__(self):
        """
        Initializes the Fractal Console.

        Args:
            None

        Returns:
            None
        """
        self.fractal = None
        self.output_path = None
        self.is_running = False
    
    def run_program(self):
        """
        Initiates the program.

        Args:
            None

        Returns:
            None
        """
        self.is_running = True
        print("Hello, this is the Fractal Generator Console. Here, you can generate \n \
              some of the most famous and well-known fractals. Please input your output directory \n \
              where you plan to store all your generated fractal images.")
        
        self.output_path = input("Enter output directory: ")
        print(f"\n\nYour current output path is now {self.output_path}!\n")
        while(self.is_running is True):
            print("Please input one of the following commands: \n \
                  [1] Create Fractal Canopy \n \
                  [2] Create Sierpinski Triangle \n \
                  [3] Create Koch Curve \n \
                  [4] Create Mandelbrot Fractal \n \
                  [5] Change output directory \n \
                  [6] Exit Program \n")
            
            user_input = input("Your input: ")
            user_input = int(user_input)

            if (user_input == 1):
                len_ratio = input("Please enter cutoff proportion (0 - 1): ")
                rot_ang = input("Please enter branching angle: ")
                iter = input("Please enter number of iterations (number of branches): ")

                tree = FractalCanopy(float(len_ratio), float(rot_ang), int(iter), self.output_path)
                tree.draw_fractal()

            if (user_input == 2):
                size = input("Please enter the size of the triangle: ")
                iter = input("Please enter the number of iterations (number of triangles): ")

                triangle = SierpinskiTriangle(int(size), int(iter), self.output_path)
                triangle.draw_fractal()

            if (user_input == 3):
                iter = input("Please enter the number of iterations (number of curves): ")

                curve = KochCurve(int(iter), self.output_path)
                curve.draw_fractal()
            
            if (user_input == 4):
                xmin = input("Please enter the minimum x range: ")
                xmax = input("Please enter the maximum x range: ")
                ymin = input("Please enter the minimum y range: ")
                ymax = input("Please enter the maximum y range: ")
                threshold = input("Please enter the Mandelbrot cutoff threshold: ")
                iter = input("Please enter the number of iterations (number of testing): ")
                res = input("Please enter the resolution (number of pixels): ")
                is_scatter = input("Please enter Y/N if you want scatter: ")

                if is_scatter.lower() == "y":
                    is_scatter = True

                else:
                    is_scatter= False
                    
                mandelbrot = MandelbrotSet((float(xmin), float(xmax)), (float(ymin), float(ymax)), \
                                           float(threshold), int(iter), int(res), is_scatter, self.output_path)
                mandelbrot.draw_fractal()

            if (user_input == 5):
                self.output_path = input("Please enter new output directory: ")

            if (user_input == 6):
                print("Thank you for using the Fractal Console!")
                self.is_running = False
            
            else:
                print("Please enter in a valid value.\n")