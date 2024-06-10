'''
* Logging Heatmap (CMP-SYN-PRO 2024)
    Author(s): Denis Komarovs, Dom Lansdale-Brown, Harry Irving, Putty Putland, Sunny Ledger
    Date: 13/06/2024
    Description: Logging Heatmap is programming project dedicated to creating software suitable to aide the local population of
                    Pu Ngaol in Cambodia in the monitoring of illegal logging activity. This software allows for the input of
                    data to represent locations around the village and utilises this data to generate a heatmap which can serve
                    as an indication of where illegal logging is happening the most.
'''
import heatmap
import string
import random

def main():
    testHeatmap1 = heatmap.Heatmap(imgPath="./map.JPG")
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

'''from heatmap_app import HeatmapApp

def main():
    app = HeatmapApp()
    app.mainloop()

if __name__ == '__main__':
    main()'''