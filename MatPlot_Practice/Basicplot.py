import numpy as np 
import matplotlib.pyplot as plt

x=np.linspace(-5,5,50)#gives values as (start,jump,end)
plt.plot(x, np.sin(x), "g-") # "g-" prints the graph betwwen these values in green colour 
plt.plot(x, np.cos(x), "r--") # r-- prints red coloured dashed lines
print(plt.show())