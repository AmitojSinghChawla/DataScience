import datetime
import matplotlib.pyplot as plt
from matplotlib import dates as mpl_dates
plt.style.use("ggplot")


dates=[
    datetime.datetime(2024, 1, 1),
    datetime.datetime(2024, 1, 2),
    datetime.datetime(2024, 1, 3),
    datetime.datetime(2024, 1, 4),
    datetime.datetime(2024, 1, 5)
]

y=[0,1,3,5,7,]


plt.plot_date(dates,y,linestyle="solid")

plt.gcf().autofmt_xdate() # get current figure and autoformats them
# i still dont get much about this technique so please remember to learn it again

date_format=mpl_dates.DateFormatter("%b, %d %y")
# In order to make our dates appear in a certain way in the plot we have imported from matplotlib dates which has a method called as DateFormater() which can print our dates in diffrent ways. The % code in the circular brackets is avaialabe in the documention for diffrent styles of formating the dates

plt.gca().xaxis.set_major_formatter(date_format)

# Now using gca (get charecter axis ) we get x axis and set its format by using set_major_formatter to the specific format which defined in the above line using DateFormatter. This now changes how the date looks on the plot

plt.show()