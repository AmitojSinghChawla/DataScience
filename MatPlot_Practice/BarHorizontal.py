import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

plt.style.use("ggplot")

# desired_width = 400
# pd.set_option('display.width', desired_width)
# np.set_printoptions(linewidth=desired_width)
# pd.set_option('display.max_columns', 20)

data = pd.read_csv("languages.csv")
data_df = pd.DataFrame(data)
lang=data_df["Language"]
column_index = data_df.columns.get_loc('Users')  # Get the index of the 'Language' column
users= data_df.iloc[:, column_index]

print(users)

plt.barh(lang,users)
plt.title("People Using Different Programming Languages")
plt.ylabel("LANGUAGES")
plt.xlabel("USERS")

plt.show()


#There is an error in the plotted graph that x labels are not proper pls fix it
