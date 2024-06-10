'''
class Heatmap:
    The Heatmap class provides functionality for all tasks surrounding the heatmap, including input of data, reading and saving of data
    to and from a file respectively, generation of the heatmap.
'''
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
import re

from datetime import date

class Heatmap:
    # Attributes
    rowsLabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    columnsLabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
# Constructor
    # The constructor takes arguments for filePath, heatmapSize, imgPath, and isGuide. The constructor will by default create an empty heatmap with grid size 10*10
    # taking the map from a local file called map.png.
    # If isGuide is flagged as true, the constructor creates a "template" heatmap which shows gridlines as a visual aide for data input.
    def __init__(self, filePath=None, heatmapSize=10, imgPath="./map.png", isGuide=False):
        self.heatmapSize = heatmapSize
        self.imgPath = imgPath
        self.heatmapData = self.loadHeatMapData(filePath)
        if isGuide:
            self.constructHeatmap(True)


# Accessor Methods
    def getHeatmapData(self):
        return self.heatmapData

# Service Methods
    # inputHeatmapData takes arguments for an alphanumeric gridCoordinate, a description, and an optional argument for number of sightings which defaults to 1.
    def inputHeatmapData(self, gridCoordinate, description, sightings=1):
        self.__logIncident__(gridCoordinate, description)
        if re.fullmatch("[a-zA-Z]{1}[0-9]+", gridCoordinate):
            alpha = gridCoordinate[0]
            numeric = gridCoordinate[1:]
            
            x, y = self.__manageInput__(alpha, numeric)

            try:
                self.heatmapData[y][x] += sightings
            except:
                print("Grid co-ordinate was not in acceptable range!")
        else:
            print("Grid Co-ordinates should follow the format \"[A-Z]{1}[0-9]+\" e.g. B6, H10 !")

    # saveHeatmapData simply writes the contents of the heatmapData attribute to a local file for storage.
    def saveHeatmapData(self):
        heatmapData = self.heatmapData
        with open('data.txt', 'w') as file:
            for i in range(0, len(heatmapData)):
                currentRow = str(heatmapData[i]).replace('[', '').replace(']', '').replace(' ', '')
                file.write(currentRow)
                if i != len(heatmapData)-1:
                    file.write("\n") 

    # loadHeatmap takes an argument "path" which is used as the file path. If no filepath is provided an empty array is constructed, if a filepath is provided
    # the method will load the data in the stored file into the heatmapData attribute.
    def loadHeatMapData(self, path=None):
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
    def constructHeatmap(self, isGuide=False):
            figName = "generatedHeatmap.jpg"

            # Create a new figure
            fig, ax = plt.subplots()

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
            ax.set_xticks(xticks)
            ax.set_xticklabels(self.columnsLabels)
            ax.set_yticks(yticks)
            ax.set_yticklabels(self.rowsLabels)

            if isGuide:
                # This block only executes if we are generating a guide grid
                
                # The figure's name is changed to alter the filename it is saved to
                figName = "guide.jpg"

                # Minor ticks are generated between the values
                xminorticks = []
                yminorticks = []
                for tick in xticks:
                    xminorticks.append(tick + xmax/20)
                for tick in yticks:
                    yminorticks.append(tick + ymin/20)

                # These minor ticks are then set on the axes
                ax.set_xticks(xminorticks, minor=True)
                ax.set_yticks(yminorticks, minor=True)  

                # The axes are then given gridlines on the minor ticks and the plot is saved as an image
                ax.grid(color="black", which="minor")
            
            # Save the figure
            fig.savefig(figName)

# Support Methods
    # The __logIncident__ method is a private method which is utilised during the inputHeatmapData method to store a log of data input.
    def __logIncident__(self, gridCoordinate, description):
        with open("log.txt", 'a') as file:
            file.write(gridCoordinate + ", " + str(date.today()) + ", " + description + "\n")

    # The __manageInput__ method is a private method which is utilised during the inputHeatmapData method to parse the alphanumeric gridCoordinate.
    def __manageInput__(self, alpha, numeric):
        x = ord(alpha.lower()) - 97
        y = 10 - int(numeric)
        if x == self.heatmapSize:
            print(alpha)
        return x, y

