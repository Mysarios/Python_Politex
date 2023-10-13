import math

Players = ["Denisov", "Petrov", "Sobolev", "Petrov", "Sobolev", "Sobolev"]
Even_numbered = len(Players) % 2

First_Team = Players[0:(math.ceil(len(Players) / 2) - Even_numbered)]
Second_Team = Players[(math.ceil(len(Players) / 2) - Even_numbered):len(Players) - Even_numbered]

print(" 1 Team = ", First_Team)
print(" 2 Team = ", Second_Team)
