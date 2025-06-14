import matplotlib.pyplot as plt
import numpy as np
import json

with open('dataset.json', 'r') as file:
    data = json.load(file)

list = data[0]
tunnusluvut = data[1]

odotusarvot = []
otoskeskihajonnat = []

for i in range(0,1000):
    otos = np.random.choice(list, 20, True)
    odotusarvot.append(float(round(np.average(otos),2)))
    otoskeskihajonnat.append(float(round(np.std(otos, ddof=1),2)))

mu_ka = np.mean(odotusarvot)
sigma_ka = np.mean(otoskeskihajonnat)

mu_label = f"Koko populaation odotusarvo {round(tunnusluvut[1],1)}"
sigma_label = f"Koko populaation keskihajonta {round(tunnusluvut[2],1)}"

mu_CI = np.percentile(odotusarvot, [2.5, 97.5])
sigma_CI = np.percentile(otoskeskihajonnat, [2.5, 97.5])

print("Odotusarvon 95% luottamusväli on [",round(mu_CI[0],2)," , ",
      round(mu_CI[1],2),"]")
print("Keskihajonnan 95% luottamusväli on [", round(sigma_CI[0],2)," , ",
      round(sigma_CI[1],2),"]")

plt.subplot(1,2,1)
plt.hist(odotusarvot, bins=25, color='royalblue', edgecolor='black')
plt.title("Odotusarvojen jakauma")
plt.xlabel(mu_label)
plt.axvline(mu_ka, color='red')
plt.axvline(mu_CI[0], color='yellow')
plt.axvline(mu_CI[1], color='yellow')

plt.subplot(1,2,2)
plt.hist(otoskeskihajonnat, bins=25, color='darkorange', edgecolor='black')
plt.title("Otoskeskihajontojen jakauma")
plt.xlabel(sigma_label)
plt.axvline(sigma_ka, color='red')
plt.axvline(sigma_CI[0], color='yellow')
plt.axvline(sigma_CI[1], color='yellow')

plt.show()