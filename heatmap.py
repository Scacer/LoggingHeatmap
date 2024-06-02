import matplotlib

class Heatmap:
    heatmapData = []
    
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
    def inputHeatmapData():
        print("Add Heatmap data here")

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



    # Support Methods
    
def main():
    print("Test Harness")

if __name__ == '__heatmap__':
    main()
