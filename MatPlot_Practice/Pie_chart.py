import matplotlib.pyplot as plt

values=[5291,5546,4754,3590]
label=['twenty',"thirty",'forty','fifty']
colors=["blue","red","green","yellow"]
explode=[0,0,0.1,0]

plt.pie(values,labels=label,wedgeprops={'edgecolor':'black'},colors=colors,explode=explode,shadow=True,startangle=90,autopct="%1.1f%%")


plt.title("Pie Chart Example")

plt.show()