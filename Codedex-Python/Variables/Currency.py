# Write code below 💖
pesos = int(input('What do you have left in pesos? '))
soles = int(input('What do you have left in soles? '))
reais = int(input('What do you have left in reais? '))
pesosToUsd = pesos * 0.00027
solesToUsd = soles * 0.29
reaisToUsd = reais * 0.19
totalInUsd = pesosToUsd + solesToUsd + reaisToUsd

print(totalInUsd)