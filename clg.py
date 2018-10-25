import time
from PIL import Image
from random import randint
su = 0
Product = [' ']
del Product[0]
Electrical_gadgets  = {'Tv':'10','Mobile':'12','Smart Watch':'20'}
Furniture = {'Bed':'10','Sofa':'12','Dinning Table':'20'}
Cloth = {'Shirt':'10','Pant':'12','T-Shirt':'20'}
iteams = ["Electrical_gadgets", "Furniture","Cloth"]
choice = input("Enter you choice B-Buy,C-Pay,D-Delete products,Q-Quit : ")
while((choice != "Q")&(len(Product)==0)):
	if(choice == "B"):
		for i in range(0,3):
			print(iteams[i])
		p = input("Enter the catagory : ")
		if( p == "Electrical_gadgets"): 
			for key,value in Electrical_gadgets.items():
				print( key,"     Price Rs ", value)
			p = input("Enter the product : ")
			Product.append(p)
			su = su + int(Electrical_gadgets.get(p))
		if( p == "Furniture"):
			for key,value in Furniture.items():
				print( key,"     Price Rs ", value)
			p = input("Enter the product : ")
			Product.append(p)
			su = su + int(Furniture.get(p))
		if( p == "Cloth"): 
			for key,value in Cloth.items():
				print( key,"     Price Rs ", value)
			p = input("Enter the product : ")
			Product.append(p)
			su = su + int(Cloth.get(p)) 
	if(choice == "C"):
		print("You're cart contains the follwing products : ",Product)
		print("THe amount to pay :", su)
		coupan = input("Any special code : ")
		if(coupan == "1234"):
				print("Total price reduced by 4%")
				su = su - su*(0.04)
		bchoice = input("Enter your choice 'credit card' 'internet banking' : ")
		if(bchoice == "Internet banking"):
			print("No internet banking facility avaiable currently")
		if(bchoice == "credit card"):
			t =0
			while(t != 3):
				cvv = list(input("Enter the cvv number :"))
				date = str(input("Enter the date number(YY-MM) :"))
				accountnumber = list(input("Enter the card number :"))
				if(date >'2018-10'):
					t = t + 1
				if(len(cvv) == 4):
					t = t + 1
				if(len(accountnumber) == 12):
					t = t +1
					if(accountnumber[0] == 5):
						print("You have Have a MASTER card ")
					if(accountnumber[0] == 4):
						print("You have Have a VISA card ")
				if(t != 3):
					print("YOu have entered some invalid detail")
					t = 0
			print("Enter the capcha to complete the payment ")
			captcha=["qgphjd","v4xbg"]
			cap = " Mime"
			x = 0
			while(captcha[x%2] != cap ):
				if(x%2 == 0):
					img = Image.open('q.png')
					img.show()
					cap = input("Enter the captcha :")
					x = x+1
					if(captcha[x%2] == cap):
						break
					img.close()
				else:	
					img = Image.open('r.png')
					img.show()
					cap = input("Enter the captcha :")
					if(captcha[x%2] == cap):
						break
					x = x + 1					
					img.close()		
			print("Payment process completed ")
			choice = "Q"
	if(choice == "D"):
		ans ="n"
		while(ans !="N"):
			i = input("Enter the element you want to delete : ")
			Product.remove(i)
			print("Product remove from cart")
			ans = input("Do you want to continiue ? Y/N ")
	if((choice == "Q")&(len(Product)==0)):
		print("Thank you for stopping by")
	elif(choice == "Q"):
		print("You have someting in cart")
	choice = input("Enter you choice B-Buy,C-Pay,D-Delete products,Q-Quit : ")
	if((choice == "Q")&(len(Product)==0)):
		print("Thank you for stopping by")
		break
	elif(choice == "Q"):
		print("You have someting in cart")













					
	

