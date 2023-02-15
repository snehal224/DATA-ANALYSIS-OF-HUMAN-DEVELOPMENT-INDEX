import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HDIfile = pd.read_csv('Book1.csv')
Hdi_journey = pd.read_csv('Book2.csv')

class M:
    def HistogramPlot_of_GNI_HDI_LifeExpectancy(self):
        Life_expectancy_list = HDIfile['Life expectancy at birth'].tolist()       # array containing Life expectancies of all countries is created
        Life_expectancy_array = np.array(Life_expectancy_list)
        Life_expectancy_array = Life_expectancy_array.astype(float)

        mean_life_expectancy = np.mean(Life_expectancy_array)
        SD_life_expectancy = np.std(Life_expectancy_array)

        HDI_list = HDIfile['Human Development Index (HDI) '].tolist()           # array containing HDIs of all countries is created
        HDI_array = np.array(HDI_list)
        HDI_array = HDI_array.astype(float)
        SD_hdi = np.std(HDI_array)
        HDI_mean = np.mean(HDI_array)

        GNI_list = HDIfile['Gross national income (GNI) per capita'].tolist()   # array containing GNIs of all countries is created
        GNI_array = np.array(GNI_list)
        GNI_array = GNI_array.astype(int)
        SD_Gni = np.std(GNI_array)
        mean_GNI = np.mean(GNI_array)

        no_of_countries = 189

        plt.hist(HDI_array, 20)
        plt.title('HDI Histogram', loc='center', fontsize=22)
        plt.xlabel('HDI', fontsize=18, color='m')
        plt.ylabel('frequency', fontsize=18, color='m')
        plt.show()

        plt.hist(GNI_array, 20)
        plt.title('GNI Histogram', loc='center', fontsize=22)
        plt.xlabel('GNI', fontsize=18, color='m')
        plt.ylabel('frequency', fontsize=18, color='m')
        plt.show()

        plt.hist(Life_expectancy_array, 20)
        plt.title('Life Expectancy Histogram', loc='center', fontsize=22)
        plt.xlabel('Life Expectancy', fontsize=18, color='m')
        plt.ylabel('frequency', fontsize=18, color='m')
        plt.show()

        # hdi_normal_dist = np.random.normal(HDI_mean, SD_hdi, no_of_countries)
        # gni_normal_dist = np.random.normal(mean_GNI, SD_Gni, no_of_countries)
        # life_expectancy_normal_dist = np.random.normal(mean_life_expectancy, SD_life_expectancy, no_of_countries)


        # plt.hist(hdi_normal_dist, 30)
        # plt.title('HDI Normal Distribution', loc='center', fontsize=22)
        # plt.show()
        #
        # plt.hist(gni_normal_dist, 30)
        # plt.title('GNI Normal Distribution', loc='center', fontsize=22)
        # plt.show()
        #
        # plt.hist(life_expectancy_normal_dist, 30)
        # plt.title('Life Expectancy Normal Distribution', loc='center', fontsize=22)
        # plt.show()
        