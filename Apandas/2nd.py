import numpy as np 
import pandas as pd

shows=pd.read_csv("shows.csv",)
shows_df=pd.DataFrame(shows)
print(shows_df)

#exporting the csv to an excel file
#shows_df.to_excel('shows.xlsx')


