'''
class Heatmap:
    The Heatmap class provides functionality for all tasks surrounding the heatmap, including input of data, reading and saving of data
    to and from a file respectively, generation of the heatmap.
'''
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
import re

class Heatmap:
    # Attributes
    rowsLabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    columnsLabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
# Constructor
    def __init__(self, filePath=None, heatmapSize=10, imgPath="./map.png"):
        self.heatmapSize = heatmapSize
        self.imgPath = imgPath
        self.heatmapData = self.loadHeatMapData(filePath)


# Accessor Methods
    def getHeatmapData(self):
        return self.heatmapData

# Service Methods
    def inputHeatmapData(self, x, y, sightings=1): #replace x, y with gridCoordinate
        self.heatmapData[y][x] += sightings
        #if re.fullmatch("[A-Z]{1}[0-9]+", gridCoordinate):
        #    print(True)
        #else:
        #    print("Grid Co-ordinates should follow the format \"[A-Z]{1}[0-9]+\" e.g. B6, H10 !")

    def saveHeatmapData(self):
        heatmapData = self.heatmapData
        with open('data.txt', 'w') as file:
            for i in range(0, len(heatmapData)):
                currentRow = str(heatmapData[i]).replace('[', '').replace(']', '').replace(' ', '')
                file.write(currentRow)
                if i != len(heatmapData)-1:
                    file.write("\n")

    def loadHeatMapData(self, path):
        if path == None:
            return [[0 for i in range(10)] for i in range(10)]
        else:
            try:
                tempArray = []
                with open(path, 'r') as file:
                    while ( currentLine := file.readline() ) != '':
                        currentRow = (currentLine.replace("\n", '')).split(",")
                        for i in range(0, len(currentRow)):
                            currentRow[i] = int(currentRow[i])  
                        tempArray.append(currentRow)
                self.heatmapSize = len(tempArray)
                return tempArray
            except:
                print("File does not exist or data is not formatted correctly!")

    # This method constructs and outputs the heatmap based on the data stored within self.heatMapData
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
            for i in range(0, self.heatmapSize):
                xticks.append( ((xmax/self.heatmapSize) * i) + (xmax/20) )
                yticks.append( ((ymin/self.heatmapSize) * i) + (ymin/20) )
            
            # Since the y axis creates labels top to bottom, we need to reverse the array
            yticks.reverse()
            
            # Plot the custom labels at the retrieved values
            plt.xticks(xticks, self.columnsLabels)
            plt.yticks(yticks, self.rowsLabels)

            # Show the plot
            plt.show()

