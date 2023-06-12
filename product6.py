# Data structure
# Data stored in RAM

pizzas =     ["small","gardenparty"]
customer = {'emailid':"venkatesh.db@gmail.com","phoneno":"9900367097"}

#  ramesh= pizza( )

cus= {"emil":"4444"}
cus["phone"]="jvt"

#        emailid                                   phoneno
#        venkatesh.db@gmail.com       9900367097 

# https://pandas.pydata.org/pandas-docs/stable/getting_started/intro_tutorials/index.html
# DataScience Data structure

# Rule pass data to function
#1. select column 2. "filename with path",data 3. sheetname
#4. coloumn name in string for plot  5. datastructure object  4. dict data for colomun renaming

# Rules' dont write  class , method's
#0.1Getting data method's       head
#     null value isna
#1.  DICT Add        colomun's  rename
#     Row based operations     Machine learning
#     Select column's which has relationship\
#2.  Copy               copy
#3.  Removedata     colomun
#4.  Searching        condition
#5.  Sort                 sort  

#6.  Plots
#7.  Statistic's
#8. data & time operation
#9.  Machine learning 


# Ms office software to open xl sheet
# Library{ pandas , csv } to open Xl sheet
# Working with FileSystem File's  Pdf ,XL,text this library work's

import pandas as pd

ds=pd.read_csv("xl sheet with path")
titanic = pd.read_csv("data/titanic.csv")
titanic.head(8)

titanic = pd.read_excel("titanic.xlsx", sheet_name="passengers")

#       Dataframe
#       emailid                                   phoneno
#  0   venkatesh.db@gmail.com       9900367097

titanic[["Age", "Sex"]]

above_35 = titanic[titanic["Age"] > 35]
class_23 = titanic[(titanic["Pclass"] == 2) | (titanic["Pclass"] == 3)]
titanic.iloc[9:25, 2:5]


air_quality = pd.read_csv("data/air_quality_no2.csv", index_col=0, parse_dates=True)
air_quality.head()
air_quality.plot()
air_quality["station_paris"].plot()
air_quality.plot.scatter(x="station_london", y="station_paris", alpha=0.5)
air_quality.plot.box()


#new colomun
air_quality["london_mg_per_cubic"] = air_quality["station_london"] * 1.882
air_quality["ratio_paris_antwerp"] = (
   ...:     air_quality["station_paris"] / air_quality["station_antwerp"]
   ...: )
air_quality_renamed = air_quality.rename(
   ...:     columns={
   ...:         "station_antwerp": "BETR801",
   ...:         "station_paris": "FR04014",
   ...:         "station_london": "London Westminster",
   ...:     }
   ...: )
   ...:

titanic.sort_values(by="Age").head()


titanic["Age"].mean()
titanic[["Age", "Fare"]].median()
titanic[["Age", "Fare"]].describe()
itanic[["Sex", "Age"]].groupby("Sex").mean()
titanic.groupby("Pclass")["Pclass"].count()

no2_subset.pivot(columns="location", values="value")

air_quality = pd.concat([air_quality_pm25, air_quality_no2], axis=0)
air_quality = pd.merge( air_quality, stations_coord, how="left", on="location")

titanic["Sex"].replace( {"male": "M", "female": "F"} )
air_quality["datetime"] = pd.to_datetime(air_quality["datetime"])
