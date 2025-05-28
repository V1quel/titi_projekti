import matplotlib.pyplot as plt
import numpy as np
import json

with open('dataset.json', 'r') as file:
    data = json.load(file)

list = data[0]
tunnusluvut = data[1]

odotusarvot = []
otoskeskihajonnat = []

for i in range(0,100):
    otos = np.random.choice(list, 10, True)
    odotusarvot.append(float(round(np.average(otos),2)))
    otoskeskihajonnat.append(float(round(np.std(otos, ddof=1),2)))

mu_ka = np.mean(odotusarvot)
sigma_ka = np.mean(otoskeskihajonnat)

mu0_label = f"Koko aineiston odotusarvo {round(tunnusluvut[3],1)}"
sigma0_label = f"Koko aineiston keskihajonta {round(tunnusluvut[4],1)}"

plt.subplot(1,2,1)
plt.hist(odotusarvot, bins=20, color='royalblue', edgecolor='black')
plt.title("Odotusarvojen jakauma")
plt.xlabel(mu0_label)
plt.axvline(mu_ka, color='red')

plt.subplot(1,2,2)
plt.hist(otoskeskihajonnat, bins=30, color='darkorange', edgecolor='black')
plt.title("Otoskeskihajontojen jakauma")
plt.xlabel(sigma0_label)
plt.axvline(sigma_ka, color='red')

plt.show()