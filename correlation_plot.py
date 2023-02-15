import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

HDIfile = pd.read_csv('Book1.csv')
Hdi_journey = pd.read_csv('Book2.csv')

class M:
    def Display_Corr_to_HDI(self):
        correlation_file = HDIfile.corr()
        corr_hdi_xaxis = []
        for x in correlation_file.index:
            corr_hdi_xaxis.append(x)
            
        corr_hdi_yaxis = correlation_file['Human Development Index (HDI) '].tolist()


        corr_hdi_xaxis_arr = np.array(corr_hdi_xaxis)
        corr_hdi_xaxis_arr = np.delete(corr_hdi_xaxis_arr, 0)
        corr_hdi_yaxis_arr = np.array(corr_hdi_yaxis)
        corr_hdi_yaxis_arr = np.delete(corr_hdi_yaxis_arr, 0)

        plt.rcParams['xtick.labelsize'] = 7
        corr_hdi_xaxis_arr[4] = 'GNI per capita'
        corr_hdi_xaxis_arr[5] = 'GNI per capita rank - HDI rank'
        plot = plt.bar(corr_hdi_xaxis_arr, corr_hdi_yaxis_arr)


        plt.title('Correlation of HDI with various factors', loc='center', fontsize=22)
        plt.xlabel('Factors', fontsize=18, color='m')
        plt.ylabel('Correlation', fontsize=18, color='m')

        plt.show()
