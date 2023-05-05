# import random library - Jenaka
import random

# setup passage of time and loop
year = 0
shouldContinue = True
# get popluation counts from user - Jenaka
prey = input("How many prey are in the ecosystem? \(RECOMMENDED TO BE IN THE UPPER 100 000s\) ")
predator = input("How many predators are in the ecosystem? \(RECOMMENDED TO BE IN THE LOWER 1000s\) ")
# start loop - Jenaka
while shouldContinue == True
  # find ratio (Melody)
  ratio = prey / predator
  # use ratio to find difficulty (Joseph)
  difficulty = ((ratio - 350)/20)+1
  # generate hunt success modifier (Joseph)
  successModifier = random.randint(85, 115)/100
  # find number of killed prey (Joseph)
  hunted = (predators * successModifier) * (17.5 * difficulty)
  # resolve prey births and deaths(Melody)
  
  # resolve predator births and deaths (Joseph)
  global predator
  predator += predator * random.randint(20, 35)/100+1
  predator -= 
  # print outputs (Melody)
  print("There are currently " + str(prey) + " left.")
  print("There are currently " + str(predator) + "left.")
  print(ratio)
    # advance time
  global year
  year +=1
  # ask user if program should continue for another 10 years
  if year % 10 == 0:
    ask = input("Would you like to continue the simulation for another 10 years? (y/n) ")
    if ask == "y":
      shouldContinue = True
    else:
      shouldContinue = False
    
