# import random library 
import random

# setup passage of time and loop
year = 0
shouldContinue = True

# get popluation counts from user
prey = input("How many prey are in the ecosystem? \(RECOMMENDED TO BE IN THE UPPER 100 000s\) ")
predator = input("How many predators are in the ecosystem? \(RECOMMENDED TO BE IN THE LOWER 1000s\) ")

# start loop
while shouldContinue == True

  # advance time
  global year
  year +=1

  # find ratio (Melody)
  ratio = prey / predator
  
  # use ratio to find difficulty
  difficulty = ((ratio - 350)/20)+1
  
  # generate hunt success modifier
  successModifier = random.randint(85, 115)/100
  
  # find number of killed prey
  hunted = (predators * successModifier) * (17.5 * difficulty)
  
  # resolve prey births and deaths
  global prey
  prey *= random.randint(10, 25)/100+1
  prey -= - hunted
  
  # resolve predator births and deaths
  global predator
  predator *= random.randint(20, 35)/100+1
  predator -= ((predators * 15) - hunted)/5
  
  # print outputs
  print("YEAR" + str(year))
  print("There are currently " + str(prey) + " left.")
  print("There are currently " + str(predator) + " left.")
  print(ratio)
  
  # ask user if program should continue for another 10 years
  if year % 10 == 0:
    ask = input("Would you like to continue the simulation for another 10 years? (y/n) ")
    if ask == "y":
      shouldContinue = True
    else:
      shouldContinue = False
    
