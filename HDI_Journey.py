import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HDIfile = pd.read_csv('Book1.csv')
Hdi_journey = pd.read_csv('Book2.csv')

class M:
    def HDI_journey_over_years(self):
        Hdi_journey = pd.read_csv('Book2.csv')
        Hdi_journey.dropna(axis=1, inplace=True)
        Hdi_journey_transpose = Hdi_journey.T

        timeline = Hdi_journey_transpose.index

        timeline = np.array(timeline)
        timeline = np.delete(timeline, 0)   # array for x axis

        India_journey = Hdi_journey_transpose[130].tolist()
        Ind_journey_array = np.array(India_journey)
        Ind_journey_array = np.delete(Ind_journey_array, 0) # plot it for India hdi over several years corresponding to timline array elements
        Ind_journey_array = Ind_journey_array.astype(float)

        Bangladesh_journey = Hdi_journey_transpose[132].tolist()
        Bangladesh_journey_array = np.array(Bangladesh_journey)
        Bangladesh_journey_array = np.delete(Bangladesh_journey_array, 0) #plot it for Bangladesh hdi over several years corresponding to timline array elements
        Bangladesh_journey_array = Bangladesh_journey_array.astype(float)

        Pakistan_journey = Hdi_journey_transpose[153].tolist()
        Pakistan_journey_array = np.array(Pakistan_journey)
        Pakistan_journey_array = np.delete(Pakistan_journey_array, 0) # plot it for Pakistan hdi over several years corresponding to timline array elements
        Pakistan_journey_array = Pakistan_journey_array.astype(float)

        China_journey = Hdi_journey_transpose[84].tolist()
        China_journey_array = np.array(China_journey)
        China_journey_array = np.delete(China_journey_array, 0) # plot it for China hdi over several years corresponding to timline array elements
        China_journey_array = China_journey_array.astype(float)


        # #individual countries
        plt.figure(figsize=(20, 8))
        plot = plt.plot(timeline, Ind_journey_array, marker='o', ms=5, mfc='r', mec='r')
        plt.title("India", fontsize=20)
        plt.xlabel('Year', fontsize=20, color='m')
        plt.ylabel('HDI', fontsize=20, color='m')
        plt.axis([None, None, 0, 1])
        plt.show()

        plt.figure(figsize=(20, 8))
        plot = plt.plot(timeline, Bangladesh_journey_array, marker='o', ms=5, mfc='r', mec='r')
        plt.title("Bangladesh", fontsize=20)
        plt.xlabel('Year', fontsize=20, color='m')
        plt.ylabel('HDI', fontsize=20, color='m')
        plt.axis([None, None, 0, 1])
        plt.show()

        plt.figure(figsize=(20, 8))
        plot = plt.plot(timeline, Pakistan_journey_array, marker='o', ms=5, mfc='r', mec='r')
        plt.title("Pakistan", fontsize=20)
        plt.xlabel('Year', fontsize=20, color='m')
        plt.ylabel('HDI', fontsize=20, color='m')
        plt.axis([None, None, 0, 1])
        plt.show()

        plt.figure(figsize=(20, 8))
        plot = plt.plot(timeline, China_journey_array, marker='o', ms=5, mfc='r', mec='r')
        plt.title("China", fontsize=20)
        plt.xlabel('Year', fontsize=20, color='m')
        plt.ylabel('HDI', fontsize=20, color='m')
        plt.axis([None, None, 0, 1])
        plt.show()
        # #graph btw timeline(years) and countries represented on y axis with their corresponding hdi over the years


        # comparison of HDI of all the 4 countries over the years

        p1 = plt.plot(timeline, Ind_journey_array, label='India', marker='o', ms=5)
        p2 = plt.plot(timeline, Pakistan_journey_array, label='Pakistan', marker='o', ms=5)
        p3 = plt.plot(timeline, Bangladesh_journey_array, label='Bangladesh', marker='o', ms=5)
        p4 = plt.plot(timeline, China_journey_array, label='China', marker='o', ms=5)

        plt.xlabel('Year', fontsize=18, color='m')
        plt.ylabel('HDI', fontsize=18, color='m')
        plt.axis([None, None, 0, 1])

        plt.legend()
        plt.title('HDI over the years', loc='center', fontsize=22)

        plt.show()