'''
    This program creates and displays an example of the classic reaction diffusion algorithim
    created by Karl Sims. This algorithim simulates a chemical reaction happening in the window.
    The whole window is initalized with "Chemical A" and as "Chemical B" is poured in or added 
    to the window, the two chemicals react and diffuse one another, resulting in a visually
    interesting peice of art. There are many different color schemes, and starting parameters, 
    that each result in thier own unique spin on this algorithim. 

    Please note that this project is powered by Pyglet, which is a module that brings the power 
    of OpenGL to Python. I am not using OpenGL, but rather the drawing API that Pyglet provides.
    This project is just scratching the surface of what Pyglet can do.

    Author: jzaunegger
    Date: 1-14-2021
'''
# Import Dependencies
import pyglet, os, sys, math
from time import time, sleep
from pyglet import clock

# Create the main class to create and control the window.
##################################################################################
class main(pyglet.window.Window):
    # Construct a new window
    def __init__(self):
        super(main, self).__init__(500, 500, "Reaction-Diffusion Algorithim", fullscreen=False, resizable=False)
        self.alive = 1
        self.refresh_rate = 60
        self.batch = pyglet.graphics.Batch()

        # Algorithim Parameters
        self.cell_size = 20
        self.seed_size = 6
        self.da = 1.0
        self.db = 0.5
        self.feed = 0.055
        self.kill = 0.062
        self.dt = 1

        self.label = pyglet.text.Label(text='', font_name='Times New Roman', font_size=18, x=10, y=10, color=(255, 0, 0, 255))
        self.rows = self.width // self.cell_size
        self.cols = self.height // self.cell_size
        self.grid = []
        self.next_grid = []

        # Initalize the grid to contain empty cells
        for x in range(self.rows):
            self.grid.append([])
            self.next_grid.append([])
            for y in range(self.cols):
                self.grid[x].append({ "A": 1, "B": 0 })
                self.next_grid[x].append({ "A": 1, "B": 0 })

        # Seed the grid
        self.seed_grid()

    def seed_grid(self):
        x_size = len(self.grid)
        y_size = len(self.grid[0])
        x_start = x_size // 2 - (self.seed_size // 2)
        y_start = y_size // 2 - (self.seed_size // 2)

        for x in range(x_start, x_start + self.seed_size):
            for y in range(y_start, y_start + self.seed_size):
                self.grid[x][y]["B"] = 1
    

    def update_grid(self):
        for x in range(1, len(self.grid)-1):
            for y in range(1, len(self.grid[x])-1):
                current_cell = self.grid[x][y]
                a = current_cell["A"]
                b = current_cell["B"]
                next_cell = self.next_grid[x][y]

                # Determine the new values
                next_cell["A"] = a + (self.da * self.laplace("A", x, y) - (a * b * b) + self.feed * (1 - a) ) * self.dt
                next_cell["B"] = b + (self.db * self.laplace("B", x, y) + (a * b * b) - (self.kill + self.feed) * b) * self.dt
                next_cell["A"] = self.constrain(next_cell["A"], 0, 1)
                next_cell["B"] = self.constrain(next_cell["B"], 0, 1)

    def laplace(self, type_str, x, y):
        if type_str == "A":
            sum_a = 0
            sum_a += self.grid[x-1][y-1]["A"] * 0.05         # Bottom Left
            sum_a += self.grid[x][y-1]["A"] * 0.2            # Bottom Middle
            sum_a += self.grid[x+1][y-1]["A"]  * 0.05         # Bottom Right
            sum_a += self.grid[x-1][y]["A"]  * 0.2            # Center Left
            sum_a += self.grid[x][y]["A"]  * -1               # Center Middle
            sum_a += self.grid[x+1][y]["A"]  * 0.2            # Center Right
            sum_a += self.grid[x-1][y+1]["A"]  * 0.05         # Top Left
            sum_a += self.grid[x][y+1]["A"]  * 0.2            # Top Middle
            sum_a += self.grid[x+1][y+1]["A"]  * 0.05         # Top Right
            return sum_a

        elif type_str == "B":
            sum_b = 0
            sum_b += self.grid[x-1][y-1]["B"] * 0.05         # Bottom Left
            sum_b += self.grid[x][y-1]["B"] * 0.2            # Bottom Middle
            sum_b += self.grid[x+1][y-1]["B"]  * 0.05         # Bottom Right
            sum_b += self.grid[x-1][y]["B"]  * 0.2            # Center Left
            sum_b += self.grid[x][y]["B"]  * -1               # Center Middle
            sum_b += self.grid[x+1][y]["B"]  * 0.2            # Center Right
            sum_b += self.grid[x-1][y+1]["B"]  * 0.05         # Top Left
            sum_b += self.grid[x][y+1]["B"]  * 0.2            # Top Middle
            sum_b += self.grid[x+1][y+1]["B"]  * 0.05         # Top Right
            return sum_b

    def swap_grids(self):
        temp = self.grid
        self.grid = self.next_grid
        self.next_grid = self.grid

    def constrain(self, var, lower, upper):
        if var < lower: return lower
        elif var > upper: return upper
        else: return var

    # Draw Loop
    def on_draw(self):
        self.render()

    # Exit the programe
    def on_close(self):
        self.alive = 0

    # Render the application out to the screen 
    def render(self):
        # Clear the screen
        self.clear()

        # Display the grid
        cells = []
        for x in range(len(self.grid)):
            for y in range(len(self.grid[x])):

                current_cell = self.next_grid[x][y]
                new_x =  x * self.cell_size
                new_y = y * self.cell_size
                c = math.floor( (current_cell["A"] - current_cell["B"]) * 255 )
                new_color = ( c, c, c)
                cells.append(pyglet.shapes.Rectangle(new_x, new_y, self.cell_size, self.cell_size, color=new_color, batch=self.batch, group=None))
 
        self.batch.draw()

        dt = clock.tick()
        self.label.text = str(math.floor(clock.get_fps()))
        self.label.draw()
            
        # For the window
        self.flip()

    # Function to run the application
    def run(self):
        while self.alive == 1:
            self.render()
            self.update_grid()
            self.swap_grids()

            event = self.dispatch_events()
            sleep(1.0/self.refresh_rate)

#######################################################################################################################

if __name__ == "__main__":
    x = main()
    x.run()