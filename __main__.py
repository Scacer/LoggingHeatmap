from heatmap_app import HeatmapApp
import heatmap
import string
import random

def main():
    app = HeatmapApp()
    app.mainloop()

    testHeatmap1 = heatmap.Heatmap()
    for i in range(0, 100):
        testString = random.choice(string.ascii_letters[0:10]) + str(random.randint(1, 10))
        testHeatmap1.inputHeatmapData(testString, "test")
    testHeatmap1.inputHeatmapData("J2", "")
    testHeatmap1.saveHeatmapData()
    testHeatmap1.constructHeatmap()

    testHeatmap2 = heatmap.Heatmap(filePath="./data.txt")
    testHeatmap2.constructHeatmap()

    testHeatmap3 = heatmap.Heatmap(isGuide=True)

if __name__ == '__main__':
    main()
