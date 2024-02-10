import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

data=sns.load_dataset("titanic")
df=pd.DataFrame(data)
abc=df["age"].dropna().tolist()
# we have got all the ages of titanic travellers

# now we create bins for histogram to categorize and divide them into
bis=[0,20,40,60,80,100]

plt.hist(abc,edgecolor="black",bins=bis)
plt.show()
#sucessfully ran