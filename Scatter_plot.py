import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HDIfile = pd.read_csv('Book1.csv')
Hdi_journey = pd.read_csv('Book2.csv')

class M:
    def ScatterPlot_bw_GNI_HDI_LifeExpectancy(self):
        GNI_list = HDIfile['Gross national income (GNI) per capita'].tolist()   # array containing GNIs of all countries is created
        GNI_array = np.array(GNI_list)
        GNI_array = np.array_split(GNI_array, 3)

        # array is divided into three each for developed, developing and underdeveloped

        GNI_Developed_countries = GNI_array[0]
        GNI_Developed_countries = GNI_Developed_countries.astype(int)

        GNI_Developing_countries = GNI_array[1]
        GNI_Developing_countries = GNI_Developing_countries.astype(int)

        GNI_Underdeveloped_countries = GNI_array[2]
        GNI_Underdeveloped_countries = GNI_Underdeveloped_countries.astype(int)

        HDI_list = HDIfile['Human Development Index (HDI) '].tolist()           # array containing HDIs of all countries is created
        HDI_array = np.array(HDI_list)
        HDI_array = np.array_split(HDI_array, 3)


        # array is divided into three each for developed, developing and underdeveloped
        HDI_Developed_countries = HDI_array[0]
        HDI_Developed_countries = HDI_Developed_countries.astype(float)

        HDI_Developing_countries = HDI_array[1]
        HDI_Developing_countries = HDI_Developing_countries.astype(float)

        HDI_Underdeveloped_countries = HDI_array[2]
        HDI_Underdeveloped_countries = HDI_Underdeveloped_countries.astype(float)


        # ## scatter diagram
        plt.scatter(HDI_Developed_countries, GNI_Developed_countries, label='Developed Countries', color='red', s=5)
        plt.scatter(HDI_Developing_countries, GNI_Developing_countries, label='Developing Countries', color='blue', s=5)
        plt.scatter(HDI_Underdeveloped_countries, GNI_Underdeveloped_countries, label='Underdeveloped Countries', color='orange', s=5)

        plt.xticks(fontsize=10)

        plt.xlabel('HDI', fontsize=18, color='m')
        plt.ylabel('GNI', fontsize=18, color='m')

        plt.legend()
        plt.title('GNI vs HDI', loc='center', fontsize=22)

        plt.show()


        # array containing Life expectancies of all countries is created
        Life_expectancy_list = HDIfile['Life expectancy at birth'].tolist()
        Life_expectancy_array = np.array(Life_expectancy_list)
        Life_expectancy_array = np.array_split(Life_expectancy_array, 3)


        # array is divided into three each for developed, developing and underdeveloped

        Life_expectancy_Developed_countries = Life_expectancy_array[0]
        Life_expectancy_Developed_countries = Life_expectancy_Developed_countries.astype(float)

        Life_expectancy_Developing_countries = Life_expectancy_array[1]
        Life_expectancy_Developing_countries = Life_expectancy_Developing_countries.astype(float)

        Life_expectancy_Underdeveloped_countries = Life_expectancy_array[2]
        Life_expectancy_Underdeveloped_countries = Life_expectancy_Underdeveloped_countries.astype(float)


        # Scatter diagram btw Life expectancy and corresponding HDI of all countries in the list
        plt.scatter(Life_expectancy_Developed_countries, HDI_Developed_countries, label='Developed Countries', color='red', s=5)
        plt.scatter(Life_expectancy_Developing_countries, HDI_Developing_countries, label='Developing countries', color='blue', s=5)
        plt.scatter(Life_expectancy_Underdeveloped_countries, HDI_Underdeveloped_countries, label='Underdeveloped Countries', color='orange', s=5)

        plt.xlabel('Life Expectancy', fontsize=18, color='m')
        plt.ylabel('HDI', fontsize=18, color='m')
 
        plt.legend()
        plt.title('HDI vs Life Expectancy', loc='center', fontsize=22)

        plt.show()

        # Scatter diagram btw Life expectancy and corresponding GNI of all countries in the list

        plt.scatter(Life_expectancy_Developed_countries, GNI_Developed_countries, label='Developed Countries', color='red', s=5)
        plt.scatter(Life_expectancy_Developing_countries, GNI_Developing_countries, label='Developing countries', color='blue', s=5)
        plt.scatter(Life_expectancy_Underdeveloped_countries, GNI_Underdeveloped_countries, label='Underdeveloped Countries', color='orange', s=5)

        plt.xlabel('Life Expectancy', fontsize=18, color='m')
        plt.ylabel('GNI', fontsize=18, color='m')

        plt.legend()
        plt.title('GNI vs Life Expectancy', loc='center', fontsize=22)
 
        plt.show()