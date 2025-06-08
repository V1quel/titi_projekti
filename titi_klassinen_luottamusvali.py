from scipy import stats
import numpy as np
import json

with open('dataset.json', 'r') as file:
    data = json.load(file)

list = data[0]
tunnusluvut = data[1]

# 95% luottamusväli on kaksisuuntainen --> 2*0,95-1=0,975
z = stats.norm.ppf(0.975)

n = tunnusluvut[0]
mu_estimate = tunnusluvut[3]
sigma_estimate = tunnusluvut[4]

mu_CI = [float(mu_estimate-z*(sigma_estimate/np.sqrt(n))),
            float(mu_estimate+z*(sigma_estimate/np.sqrt(n)))]

sigma_CI = [float(sigma_estimate-z*(sigma_estimate/np.sqrt(n))),
            float(sigma_estimate+z*(sigma_estimate/np.sqrt(n)))]

print("Odotusarvon luottamusväli on:", mu_CI)
print("Keskihajonnan luottamusväli on:", sigma_CI)