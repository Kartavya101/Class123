# Project 123
import numpy as np
rewards = np.array([10,9,8,7,6,5,4,3,2,1])
print("Available Awards Are: \n",rewards)
def shoot():
  return np.random.randint(0,11)

action = shoot()
print("You Hit ring number:",action) 
for i in rewards:
  if i == action:
    print("reward is: ", action, "points!")
