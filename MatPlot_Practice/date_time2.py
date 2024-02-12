import datetime
import matplotlib.pyplot as plt
import pytz
import pandas as pd

data=pd.read_csv("datafile.csv")
data_df=pd.DataFrame(data)

profits=data_df["Profit"]
dates=data_df["Date"]

plt.plot_date(dates,profits,linestyle="solid")
# A very important thing to remember here is right now the plot is considering dates to be strings and not of the format of
#of date time that is why if you add another row to the csv the date would appear last in graph but not according the
#order in which date should occur eg if i add a row with date as 2017 it would still appear after 2019 beacuse it isnt treating dates as datetime.

# to do that we do some pandas operations like this
data_df["Date"]=pd.to_datetime(data_df["Date"])
data_df.sort_values("Date",inplace=True)# this sorts the column of dates and
#very imprortant thing the keyword "inplace" applies the settings the variable. like if i said df=date.sort_values("Date") then the variable df contains sorted dates column but -------->>>> date.sort_values("Date",inplace=True) using inplace here sorts the dates in the original column of the imported Data Frame.
plt.show()