import matplotlib.pyplot as plt
import numpy as np
import json

list = []
tunnusluvut = []

data = [
    list,
    tunnusluvut
]

mu = np.random.randint(-100,101)
sigma = np.random.randint(1,26)

for i in range(0,1000):
    x = np.random.normal(mu, sigma)
    list.append(x)

mu0 = np.mean(list)
sigma0 = np.std(list)
n = len(list)

print(n)

tunnusluvut.append(n)
tunnusluvut.append(mu)
tunnusluvut.append(sigma)
tunnusluvut.append(mu0)
tunnusluvut.append(sigma0)

with open('dataset.json', 'w') as file:
    json.dump(data, file)

plt.hist(list, bins=30, edgecolor='black')
plt.xlabel("Havainnon arvo")
plt.ylabel("Havaintojen määrä")
plt.show()