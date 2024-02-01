import numpy as np
import pandas as pd

file= pd.read_excel('Historicalinvesttemp.xlsx')
file_df = pd.DataFrame(file)
print(file_df.head)
#Exporting the Xlsx to Csv
file_df.to_csv('investment.csv')

#OpenPyXL is a library i had to download as pandas uses it as a 3rd party to read and write excel files