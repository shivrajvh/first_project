'''
import random

playerhealth = 500
enemyhealthl=60
enemyhealthh=85

while playerhealth >= 0:
	random_no=random.randrange(enemyhealthl, enemyhealthh)
	playerhealth = playerhealth - random_no

	if playerhealth <= 10:
		print ("Player health is critical. Exiting Game")


	if playerhealth > 10:
		print("Enemy attacked for", random_no,"points. Balance health is,", playerhealth)

'''

def main():
	x=0
	#define a while loop
	while(x <= 4):
		print(x)
		x = x+1

if __name__ == "__main__":
    main()
