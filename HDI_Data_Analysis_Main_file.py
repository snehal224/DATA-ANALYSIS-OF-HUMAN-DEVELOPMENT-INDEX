try:
    from numpy.core.numeric import correlate

except ImportError:  # exception if imported module is not present
    print("please enter a valid module")

from numpy.core.numeric import correlate
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import correlation_plot
import HDI_Journey
import Scatter_plot
import Histogram_plot

HDIfile = pd.read_csv('Book1.csv')
Hdi_journey = pd.read_csv('Book2.csv')

# exceptions: if in data HDI rank of any country occurs negative
# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


class Invalid(Exception):
    msg1 = "HDI rank of country cannot be zero or negative please enter a valid data"


for x in HDIfile.index:
    try:

        if HDIfile.loc[x, 'HDI rank'] <= 0:
            raise Invalid

    except Invalid as e:
        print(e.msg1)

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ##MODULE1
# #correlation of HDI to other factors

#  bar graph of correlation of different factors to HDI
#  x axis has all parameters
#  y axis has correlation values correspondingly


object = correlation_plot.M()
object.Display_Corr_to_HDI()


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------


# ##MODULE2
# #graph of journey of different countries HDI over years

object = HDI_Journey.M()
object.HDI_journey_over_years()



# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ##MODULE3
# #creating a function prototype which takes input the country name(First letter capital), and displays its HDI parameters

# #taking valid country name  from user using exception handling



class Invalid_Name(Exception):
    msg = "First letter of country name should always be a capital letter and name should not contain any number"


while True:
    try:
        country = input("Enter country name :")
        if country[0].islower():
            raise Invalid_Name
        elif country[0].isupper():
            for c in country:
                if c.isdigit():
                    raise Invalid_Name
        break
    except Invalid_Name as Err:
        print(Err.msg)


# #####################################
def Display_Country_info(Countries, Country):

  Hdi_finder_keys = HDIfile[Countries].tolist()  # creating dictionary to find the SNo of that country in the list
  Hdi_finder_values = HDIfile.index.tolist()

  Hdi_finder = dict(zip(Hdi_finder_keys, Hdi_finder_values))  # dictionary to find the SNo created
  HDIfile_transpose = HDIfile.T


# name error exception
  try:
    Hdi_parameters = HDIfile_transpose.index.tolist()  # creating list which contains parameters of HDI
    Hdi_parameters_of_country = HDIfile_transpose[Hdi_finder[country]].tolist()  # creating list which has values of HDI parameters for corresponding country

  except NameError:
    print("some variable is not defined")



  Display_info = dict(zip(Hdi_parameters, Hdi_parameters_of_country))  # clubbing above two list into a dictionary
  print(Display_info)  # display all info of that particular country

# #######################################

Display_Country_info('Countries', country)


# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ##MODULE4
# #Scatter diagram btw HDI and corresponding GNI of all countries in the list

object = Scatter_plot.M()
object.ScatterPlot_bw_GNI_HDI_LifeExpectancy()

# --------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------

# ##MODULE5
# #Histogram of GNI per capita, HDI and life expectancy

object = Histogram_plot.M()
object.HistogramPlot_of_GNI_HDI_LifeExpectancy()





