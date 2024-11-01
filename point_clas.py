import matplotlib.pyplot as plt

class ScatterPlotter:                                              #create class named ScatterPlotter
    def __init__(self, file):                                      #initialize the class
        """Initialize the ScatterPlotter with a file path."""
        self.file = file                                           #declare variables
        self.x = []
        self.y = []
        self.translated_x = []
        self.translated_y = []
        self.plotter()

        # Load coordinates from the file


    def plotter(self):  # define plotter function
        with open(self.file, "r") as f:  # open file object as f
            f.readline()  # remove first line from file
            f = f.readlines()  # read the rest of the lines in the file
        for row in f:  # for every line in the file
            self.y.append(float(row.split(",")[0]))  # add the first figure to list y
            self.x.append(float(row.split(",")[1]))  # and the second to list x
        print(f'y_coords = {self.y}, \n x_coords = {self.x}')
        plt.scatter(self.x, self.y, color='green', label='Original_Points')
        plt.scatter(self.translated_x, self.translated_y, color='yellow', label='Translated_Points') # draw scatter plot
        plt.xlabel("X VARIABLE")  # x axis label
        plt.ylabel("Y VARIABLE")  # y axis label
        plt.title("SCATTER PLOT FUNCTION")  # plot title
        plt.grid(False)  # show grid
        plt.show()  # display plot

    def translate_points(self, dx, dy):
        """Translate the points by a given offset (dx, dy)."""
        self.translated_x = [x + dx for x in self.x]
        self.translated_y = [y + dy for y in self.y]

# Usage
def path(): #define user input function
    file = (input(f"Please enter your text file directory path: ")) #get user input
    print("\n", f'"{file}"', "\n")
    if __name__ == "__main__":
        plot = ScatterPlotter(file)
        plot.translate_points(dx=1, dy=1)  # Example translation
        plot.plotter()

path()
