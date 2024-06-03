import math
import matplotlib.image as image
import matplotlib.pyplot as plt
import numpy as np

import matplotlib
import matplotlib as mpls

class Heatmap:
    imgPath = ("D:\\Code\\Python\\LoggingHeatmap\\LoggingHeatmap\\map.png")
    heatmapData = []
    rowsLabels = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '10']
    columnsLabels = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
    
    # Constructor
    def __init__(self, filepath=None):
        if filepath == None:
            self.heatmapData = [[0 for i in range(10)] for i in range(10)]
        else:
            with open(filepath) as file:
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
                    print(column, row)
                    file.write(str(row))
                    if rowcount != 10:
                        file.write(",")
                if columncount != 10:
                    file.write("\n")

    def constructHeatmap(self):
            plt.figure()
            
            img = plt.imread(self.imgPath)
            plt.imshow(img, alpha=1)

            xmin, xmax = plt.xlim()
            ymin, ymax = plt.ylim()

            Mat = np.array(self.heatmapData)
            plt.imshow(Mat, cmap='Reds', interpolation='nearest', alpha=0.5, extent=(xmin, xmax, ymin, ymax))
            
            xticks = []
            yticks = []
            for i in range(0, 10):
                xticks.append( ((xmax/10) * i) + (xmax/20) )
                yticks.append( ((ymin/10) * i) + (ymin/20) )
            yticks.reverse()
            
            plt.xticks(xticks, self.columnsLabels)
            plt.yticks(yticks, self.rowsLabels)

            plt.show()
        

        

    # Support Methods
    
def main():
    print("Test Harness")

if __name__ == '__heatmap__':
    main()
