import heatmap

def main():
    testHeatmap1 = heatmap.Heatmap()
    print(testHeatmap1.getHeatmapData())
    testHeatmap1.saveHeatmapData()
    

if __name__ == '__main__':
    main()