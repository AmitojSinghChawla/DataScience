import matplotlib.pyplot as plt
plt.style.use('Solarize_Light2')

#This is the data of a game where for every minute score of
#a player is being displayed for Eg in the 1st minute
#player 1 has 1 point in 2nd minute he scores
# another point and his total becomes 2 #
#similarly in the 3rd minute he socres another
#making a total of 3 points to his name
# that is how all payer points are given below
minutes=[1,2,3,4,5,6,7,8,9]
labels=["player1","player2","player3"]

player1=[1,2,3,3,4,4,4,4,5]
player2=[1,1,1,1,2,2,2,3,4]
player3=[1,1,1,2,2,2,3,3,3]

plt.stackplot(minutes,player1,player2,player3 , labels=labels)
plt.legend(loc="upper left")
plt.show()
