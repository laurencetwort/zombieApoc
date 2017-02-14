import random

class main ():

	def humans(self,zombiePop, humanPop, infected, day):
		
		if day < 30:
			famine = 0 
		elif day < 90:
			famine = humanPop * (random.uniform(0, 0.001))
		elif day < 180:
			famine = humanPop * (random.uniform(0, 0.005))
		else:
			famine = humanPop * (random.uniform(0, 0.001))
		
		if day < 5:
			conflict = 0
		else:
			conflict = humanPop * (random.uniform(0, 0.001))
		
		accident = humanPop * (random.uniform(0, 0.0001))
		
		if day < 90:
			illness = 0
		elif day < 180:
			illness = humanPop * (random.uniform(0, 0.0001))
		elif day < 270:
			illness = humanPop * (random.uniform(0, 0.001))
		elif day < 360:
			illness = humanPop * (random.uniform(0, 0.002))
		else:
			illness = humanPop * (random.uniform(0, 0.003)+(day/2*0.001))#trying to simulate increased age/ accumlulation of injuries3
		
		reproduction = humanPop * (random.uniform(0, 0.003041095893))

		amount = illness + accident + conflict + famine + infected - reproduction

		return int(amount),int(illness),int(conflict),int(famine),int(reproduction),int(accident)

	def zombies(self,zombiePop, humanPop, infected, day):

		conflict = humanPop * (random.uniform(0, 0.01))
		accident = zombiePop * (random.uniform(0, 0.001))
		wearNtear = zombiePop * (random.uniform(0, 0.01)+(day/2*0.001))
		amount = infected - conflict - accident - wearNtear
		
		return int(amount)

	def infection(self, humanPop, zombiePop):
		
		amount = humanPop * (random.uniform(0, 0.1))
		
		return int(amount)

	def zombieApoc(self, originalHumanPop, zombPop):
		
		humanPop = originalHumanPop
		zombiePop = zombPop
		day = 0
		illness = 0
		conflict = 0
		famine = 0
		reproduction = 0
		infected2 = 0
		accident = 0
		
		while (1==1):
			
			infected = self.infection(humanPop,zombiePop)
			infected2 = infected2 + infected
			zombiePop = zombiePop + self.zombies(zombiePop, humanPop, infected, day)
			humans = self.humans(zombiePop, humanPop, infected, day)
			humanPop = humanPop - humans[0]
			illness = illness + humans[1]
			conflict = conflict + humans[2]
			famine = famine + humans[3]
			reproduction = reproduction + humans[4]
			infected2 = infected2 + infected
			accident = accident + humans[5]
			day = day + 1
			
			if humanPop <= 0:
				humanPop = 0
				return(day,humanPop,zombiePop,illness,conflict,famine,reproduction,infected2,accident)
				break
			
			if zombiePop <= 0:
				zombiePop = 0
				return(day,humanPop,zombiePop,illness,conflict,famine,reproduction,infected2,accident)
				break
	
	def __init__(self):

		a = self.zombieApoc(7000000000,1)
		if a[1] > 10000:
			result = 'The Zombie Appocalypse has so far been Averted'
			print(a[1])
		else:
			result = 'The Human Race has Been Destroyed'
			human = 'Humans Left alive: '
			human += str(a[1])
			print(human)
		string = 'Zombie Appocalypse took: '
		string += str((a[0])/365)
		string += ' Years '
		string += str((a[0])%365)
		string += ' Days'
		print(result)
		print(string)

if __name__ == "__main__":
        main() 
