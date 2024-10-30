import matplotlib.pyplot as plt  #import matplot module


def plotter(file):  #define plotter function
    x = []  # declare empty list x
    y = []  #declare empty list y
    with open(file, "r") as f:  #open file object as f
        f.readline()  #remove first line from file
        f = f.readlines()  #read the rest of the lines in the file
    for row in f:  #for every line in the file
        y.append(float(row.split(",")[0]))  #add the first figure to list y
        x.append(float(row.split(",")[1]))  #and the second to list x
    print(f'y_coords = {y}, \n x_coords = {x}')
    plt.scatter(x, y)  #draw scatter plot
    plt.xlabel("x variable")  #x axis label
    plt.ylabel("y variable")  #y axis label
    plt.title("SCATTER PLOT FUNCTION")  #plot title
    plt.grid(False)  #show grid
    plt.show()  #display plot


def path(): #define user input function
    file = (input(f"Please enter a directory path: ")) #get user input
    print("\n", f'"{file}"', "\n")
    plotter(file)


path() #run program
