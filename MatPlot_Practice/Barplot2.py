import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

desired_width = 400
pd.set_option('display.width', desired_width)
np.set_printoptions(linewidth=desired_width)
pd.set_option('display.max_columns', 20)

data = pd.read_csv("air_traffic.csv")
data_df = pd.DataFrame(data)

# rows =108
# columns = 10
# subset = data_df.head(rows).iloc[:, :columns]
# # print(subset)

# Calculate total international flights per year
total_flights_per_year = data_df.groupby('Year')["Flights"].sum().tolist()


# Get unique years
unique_years = data_df['Year'].unique().tolist()


# # Print the total international flights per year and unique years
# print("Total international flights per year:", total_flights_per_year)
# print("Unique years:", unique_years)

plt.bar(unique_years, total_flights_per_year, color='skyblue')
plt.title("No of International FLights from USA per Year")
plt.xlabel("YEARS")
plt.ylabel("NO OF FLIGHTS")
plt.show()