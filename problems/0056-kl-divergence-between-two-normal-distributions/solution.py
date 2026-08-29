import numpy as np
import math 

def kl_divergence_normal(mu_p, sigma_p, mu_q, sigma_q):
	log = np.log(sigma_q / sigma_p)
	nom = (sigma_p**2 + (mu_p - mu_q)**2) 
	denom = 2*sigma_q**2
	res = log + (nom / denom) - (1/2)

	if denom == 0:
		return 0.0
	else:
		return res
