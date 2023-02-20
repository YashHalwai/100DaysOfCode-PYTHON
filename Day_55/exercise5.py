# Exercise 5 - Snake Water Gun | Python Tutorial - Day #55

# https://www.youtube.com/watch?v=dDsh7FT6-0I&list=PLu0W_9lII9agwh1XjRt242xIpHhPT2llg&index=55


import random
def swg():
	print("Enter your name")
	name = str(input())
	print("Enter no. of round you want to play")
	n = int(input())
	time = 0
	p = 0
	c = 0
	print("ok %s here is rule"%name)
	print("[RULES]:-\n1)Snake is win from Water but lose from Gun\n2)Water is win from Gun but lose from snake\n3)Gun is win from snake but lose from Water")
	com = "because computer write"
	while(time<n):
		type = ['Snake', 'Water', 'Gun']
		r = random.choice(type)
		turn = str(input("\nEnter Snake or Water or Gun:\n"))
		if turn==r:
			print("\ndraw ")
		elif turn=="Snake" and r=="Water":
			p = p+1
			print("\nYou win")
		elif turn=="Snake" and r=="Gun":
			c = c+1
			print("\nYou lose")
		elif turn=="Water" and r=="Snake":
			c=c+1
			print("\nYou lose")
		elif turn=="Water" and r=="Gun":
			p = p+1
			print("\nYou win")
		elif turn=="Gun" and r=="Water":
			c=c+1
			print("\nYou lose")
		elif turn=="Gun" and r=="Snake":
			p=p+1
			print("\nYou win")
		else :
			print("\n[error occur]: Unexpected name")
		time = time+1
	if p<c:
		print("computer win")
	elif p==c:
		print("Draw")
	else:
		print("%s you win"%name)
if __name__ == '__main__':
	swg()