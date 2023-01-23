
import random
n = random.randint(1,5)
for i in range(5):
	nn = int(input("enter a number :"+'\n'))
	if n==nn:
		print('you got it mowa')
		break
	else:
		print("try agani mowa")
		print("you have only",4-i,'chances left','\n')
	
