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
import random

def main():
    testHeatmap1 = heatmap.Heatmap()
    #for i in range(0, 100):
    #    testHeatmap1.inputHeatmapData(random.randint(0, 9), random.randint(0, 9))
    testHeatmap1.saveHeatmapData()
    testHeatmap1.constructHeatmap()
    

if __name__ == '__main__':
    main()