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
        graphData = np.array(self.heatmapData)

        fig, ax = plt.subplots()
        im = ax.imshow(graphData)

        ax.set_xticks(np.arange(len(self.rowsLabels)), labels=self.rowsLabels)
        ax.set_yticks(np.arange(len(self.columnsLabels)), labels=self.columnsLabels)

        plt.setp(ax.get_xticklabels(), rotation=45, ha="right", rotation_mode="anchor")

        for i in range(len(self.columnsLabels)):
            for j in range(len(self.rowsLabels)):
                text = ax.text(j, i, graphData[i, j], ha="center", va="center", color="w")


        ax.set_title("Illegal Logging Activity")
        fig.tight_layout()
        plt.show()
        

    # Support Methods
    
def main():
    print("Test Harness")

if __name__ == '__heatmap__':
    main()
