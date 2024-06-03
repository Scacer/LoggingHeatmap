import heatmap

def main():
    testHeatmap1 = heatmap.Heatmap()
    print(testHeatmap1.getHeatmapData())
    testHeatmap1.inputHeatmapData(2, 5)
    testHeatmap1.saveHeatmapData()
    testHeatmap1.constructHeatmap()
    

if __name__ == '__main__':
    main()