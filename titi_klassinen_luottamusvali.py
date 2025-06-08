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

CI_lower_limit = mu_estimate-z*(sigma_estimate/np.sqrt(n))
CI_upper_limit = mu_estimate+z*(sigma_estimate/np.sqrt(n))

print("Luottamusvälin alaraja on:", CI_lower_limit)
print("Luottamusvälin yläraja on:", CI_upper_limit)