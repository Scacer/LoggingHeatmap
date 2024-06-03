'''
class Heatmap:
    The Heatmap class provides functionality for all tasks surrounding the heatmap, including input of data, reading and saving of data
    to and from a file respectively, generation of the heatmap.
'''
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np

class Heatmap:
    # Attributes
    heatmapData = []
    rowsLabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    columnsLabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    # Constructor
    def __init__(self, filePath=None, imgPath="./map"):
        self.imgPath = imgPath
        if filePath == None:
            self.heatmapData = [[0 for i in range(10)] for i in range(10)]
        else:
            with open(filePath) as file:
                self.heatmapData = file.read()


    # Accessor Methods
    def getHeatmapData(self):
        return self.heatmapData
        

    # Service Methods
    def inputHeatmapData(self, x, y, sightings=1):
        self.heatmapData[y][x] += sightings

    def saveHeatmapData(self):
        with open('data.txt', 'w') as file:
            columncount = 0
            for column in self.heatmapData:
                rowcount = 0
                columncount += 1
                for row in column:
                    rowcount +=1
                    file.write(str(row))
                    if rowcount != 10:
                        file.write(",")
                if columncount != 10:
                    file.write("\n")

    def constructHeatmap(self):
            # Create a new figure
            plt.figure()

            # Read the map image and plot it first so that the plot size equals image size
            img = plt.imread(self.imgPath)
            plt.imshow(img, alpha=1)

            # Retrieve the minimum and maximum values of the plot axes
            xmin, xmax = plt.xlim()
            ymin, ymax = plt.ylim()

            # Create a matrix for the heatmap from the data stored within the object
            matrix = np.array(self.heatmapData)

            # Plot the matrix, scale it to plot size and set opacity to 0.5
            plt.imshow(matrix, cmap='Reds', interpolation='nearest', alpha=0.5, extent=(xmin, xmax, ymin, ymax))
            
            # Retrieve the values for which to create custom labels
            xticks = []
            yticks = []
            for i in range(0, 10):
                xticks.append( ((xmax/10) * i) + (xmax/20) )
                yticks.append( ((ymin/10) * i) + (ymin/20) )
            
            # Since the y axis creates labels top to bottom, we need to reverse the array
            yticks.reverse()
            
            # Plot the custom labels at the retrieved values
            plt.xticks(xticks, self.columnsLabels)
            plt.yticks(yticks, self.rowsLabels)

            # Show the plot
            plt.show()
        

        

    # Support Methods
    
def main():
    print("Test Harness")

if __name__ == '__heatmap__':
    main()
