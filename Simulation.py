# import random library 
import random

# setup passage of time and loop
year = 0
shouldContinue = True

# get popluation counts from user
prey = int(input("How many prey are in the ecosystem? \(RECOMMENDED TO BE IN THE UPPER 100 000s\) "))
predator = int(input("How many predators are in the ecosystem? \(RECOMMENDED TO BE IN THE LOWER 1000s\) "))

# start loop
while shouldContinue == True:

  # advance time
  year +=1

  # find ratio 
  ratio = prey / predator
  print("The starting ratio is " + str(ratio))
  
  # use ratio to find difficulty
  difficulty = ((ratio - 350)/20)+1
  
  # generate hunt success modifier
  successModifier = random.randint(85, 115)/100
  
  # find number of killed prey
  hunted = (predator * successModifier) * (17.5 * difficulty)
  
  # resolve prey births and deaths
  prey *= random.randint(5, 8)/100+1
  prey -= - hunted
  if hunted > prey:
    prey = 0
  
  # resolve predator births and deaths
  predator *= random.randint(20, 35)/100+1
  predator -= ((predator * 15) - hunted)/5
  predator *= .85
  if predator < 0:
    predator = 0
  
  # print outputs
  print("YEAR" + str(year))
  print("There are currently " + str(prey) + " prey left.")
  print("There are currently " + str(predator) + " predators left.")
  print("Prey/Predator ratio = " + str(ratio))
  
  # ask user if program should continue for another 10 years
  if year % 10 == 0:
    ask = input("Would you like to continue the simulation for another 10 years? (y/n) ")
    if ask == "y":
      shouldContinue = True
    else:
      shouldContinue = False
    
