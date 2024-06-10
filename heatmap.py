import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np
import re

from datetime import date

class Heatmap:
    rowsLabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    columnsLabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']

    def __init__(self, filePath=None, heatmapSize=10, imgPath="./map.png", isGuide=False):
        self.heatmapSize = heatmapSize
        self.imgPath = imgPath
        self.heatmapData = self.loadHeatMapData(filePath)
        if isGuide:
            self.constructHeatmap(True)
        print("Heatmap initialized with size:", self.heatmapSize)

    def getHeatmapData(self):
        return self.heatmapData

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

    def saveHeatmapData(self):
        heatmapData = self.heatmapData
        with open('data.txt', 'w') as file:
            for i in range(0, len(heatmapData)):
                currentRow = str(heatmapData[i]).replace('[', '').replace(']', '').replace(' ', '')
                file.write(currentRow)
                if i != len(heatmapData)-1:
                    file.write("\n")
        print("Heatmap data saved to data.txt")

    def loadHeatMapData(self, path):
        if path is None:
            return [[0 for i in range(10)] for i in range(10)]
        else:
            try:
                tempArray = []
                with open(path, 'r') as file:
                    while (currentLine := file.readline()) != '':
                        currentRow = (currentLine.replace("\n", '')).split(",")
                        for i in range(0, len(currentRow)):
                            currentRow[i] = int(currentRow[i])
                        tempArray.append(currentRow)
                self.heatmapSize = len(tempArray)
                print("Heatmap data loaded from:", path)
                return tempArray
            except:
                print("File does not exist or data is not formatted correctly!")

    def constructHeatmap(self, isGuide=False):
        figName = "generatedHeatmap.jpg"
        fig, ax = plt.subplots()
        img = plt.imread(self.imgPath)
        plt.imshow(img, alpha=1)

        xmin, xmax = plt.xlim()
        ymin, ymax = plt.ylim()

        matrix = np.array(self.heatmapData)
        plt.imshow(matrix, cmap='Reds', interpolation='nearest', alpha=0.5, extent=(xmin, xmax, ymin, ymax))

        xticks = []
        yticks = []
        for i in range(0, self.heatmapSize):
            xticks.append(((xmax/self.heatmapSize) * i) + (xmax/20))
            yticks.append(((ymin/self.heatmapSize) * i) + (ymin/20))

        yticks.reverse()
        ax.set_xticks(xticks)
        ax.set_xticklabels(self.columnsLabels)
        ax.set_yticks(yticks)
        ax.set_yticklabels(self.rowsLabels)

        if isGuide:
            figName = "guide.jpg"
            xminorticks = []
            yminorticks = []
            for tick in xticks:
                xminorticks.append(tick + xmax/20)
            for tick in yticks:
                yminorticks.append(tick + ymin/20)
            ax.set_xticks(xminorticks, minor=True)
            ax.set_yticks(yminorticks, minor=True)
            ax.grid(color="black", which="minor")

        fig.savefig(figName)
        print(f"Heatmap saved as {figName}")

    def __logIncident__(self, gridCoordinate, description):
        with open("log.txt", 'a') as file:
            file.write(gridCoordinate + ", " + str(date.today()) + ", " + description + "\n")
        print(f"Incident logged: {gridCoordinate}, {description}")

    def __manageInput__(self, alpha, numeric):
        x = ord(alpha.lower()) - 97
        y = 10 - int(numeric)
        return x, y
