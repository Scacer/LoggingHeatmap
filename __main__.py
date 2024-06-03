import heatmap
import random

def main():
    testHeatmap1 = heatmap.Heatmap()
    print(testHeatmap1.getHeatmapData())
    for i in range(0, 100):
        testHeatmap1.inputHeatmapData(random.randint(0, 9), random.randint(0, 9))
    testHeatmap1.saveHeatmapData()
    testHeatmap1.constructHeatmap()
    

if __name__ == '__main__':
    main()