import matplotlib.pyplot as plt
import numpy as np

class Heatmap:
    rowsLabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    columnsLabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    def __init__(self, filePath=None, heatmapSize=10, imgPath="map.png"):
        self.heatmapSize = heatmapSize
        self.imgPath = imgPath
        self.heatmapData = self.loadHeatMapData(filePath)

    def getHeatmapData(self):
        return self.heatmapData

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
                    if rowcount != self.heatmapSize:
                        file.write(",")
                if columncount != self.heatmapSize:
                    file.write("\n")

    def loadHeatMapData(self, path):
        if path == None:
            return [[0 for i in range(10)] for i in range(10)]
        else:
            try:
                tempArray = []
                with open(path, 'r') as file:
                    for currentLine in file:
                        currentRow = [int(value) for value in currentLine.strip().split(",")]
                        tempArray.append(currentRow)
                self.heatmapSize = len(tempArray)
                print(tempArray)
                return tempArray
            except FileNotFoundError:
                print("File does not exist!")
            except ValueError:
                print("Data is not formatted correctly!")

    def constructHeatmap(self):
            plt.figure()
            img = plt.imread(self.imgPath)
            plt.imshow(img, alpha=1)
            xmin, xmax = plt.xlim()
            ymin, ymax = plt.ylim()
            matrix = np.array(self.heatmapData)
            plt.imshow(matrix, cmap='Reds', interpolation='nearest', alpha=0.5, extent=(xmin, xmax, ymin, ymax))
            xticks = []
            yticks = []
            for i in range(0, self.heatmapSize):
                xticks.append( ((xmax/self.heatmapSize) * i) + (xmax/20) )
                yticks.append( ((ymin/self.heatmapSize) * i) + (ymin/20) )
            yticks.reverse()
            plt.xticks(xticks, self.columnsLabels)
            plt.yticks(yticks, self.rowsLabels)
            plt.show()

def main():
    print("Test Harness")

if __name__ == 'heatmap':
    main()
