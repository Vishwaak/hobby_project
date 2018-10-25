#No draw situtaion only win or lose
#stone paper scissors game implementation
import random
str = input("your input: ")
ar = ["stone","paper","scissors"]
comp = random.randrange(0,2) #rand for comp choice
choice = ar[comp]
#computer's numerical choice)
i=-1
user=0
while (i == -1):
	if(str == ar[0]):  #to find the choice of the user
		i=0
	if( str == ar[1]):
		i = 1
	if( str == ar[2]):
		i = 2
	user = i
	if(i == -1):
		str = input("Invalid input enter again : ")
while(choice == str):
	comp = random.randrange(0,2)
	choice = ar[comp] 
print("Computer choice :",choice)
if(abs(comp - user) -2 != 0): #can't use the or and as they will fail the case of 2,1 
	if(comp > user ):
		print ("Computer wins")
	else:
		print ("user wins")
if(comp == 2) & (user == 0):
	print("User Wins")
if(comp == 0) & (user == 2):
	print("Computer Wins")

