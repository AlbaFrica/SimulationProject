# import random library 
import random

# setup passage of time and loop
year = 0
shouldContinue = True

# get popluation counts from user
prey = int(input("How many prey are in the ecosystem? \(RECOMMENDED TO BE IN THE UPPER 100000s\) "))
predator = int(input("How many predators are in the ecosystem? \(RECOMMENDED TO BE IN THE LOWER 1000s\) "))

# find ratio (Melody)
ratio = prey / predator
print("The starting ratio is " + str(ratio))

# start loop
while shouldContinue == True:

  # advance time
  year +=1
  
  # use ratio to find difficulty
  difficulty = ((ratio - 350)/20)+1
  
  # generate hunt success modifier
  successModifier = random.randint(85, 115)/100
  
  # find number of killed prey
  hunted = (predator * successModifier) * (17.5 * difficulty)
  
  # resolve prey births and deaths
  prey *= (random.randint(15, 18)/100)+1
  prey -= hunted
  if prey < 0:
    prey = 0
  prey = int(prey)
  
  
  # resolve predator births and deaths
  predator *= random.randint(20, 35)/100+1
  shouldStarve = ((predator * 15) - hunted)/15
  if shouldStarve > 0:
    predator -= shouldStarve
  predator *= .85
  if predator < 0:
    predator = 0
  predator = int(predator)

  # print outputs
  print("YEAR" + str(year))
  print("There are currently " + str(prey) + " prey left.")
  print("There are currently " + str(predator) + " predators left.")

  # find new ratio
  if predator != 0:
    ratio = prey / predator
    print("Prey/Predator ratio = " + str(round(ratio, 2)))
  
  # ask user if program should continue for another 10 years
  if year % 10 == 0:
    ask = input("Would you like to continue the simulation for another 10 years? (y/n) ")
    if ask == "y":
      shouldContinue = True
    else:
      shouldContinue = False
    
