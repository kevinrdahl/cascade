import random

def uniform(network, max, min):
	return [(i,random.uniform(max, min)) for i in range(len(network))]

def normal(network, mean, sigma):
	return [(i,random.normalvariate(mean, sigma)) for i in range(len(network))]

def longtail(network, max, min, power):
	return [(i,powerlaw(max, min, power)) for i in range(len(network))]

def powerlaw(max, min, power):
	rand = random.uniform(max, min)
	ret = ((max**(power+1) - min**(power+1))*rand + min**(power+1))**(1/(power+1))
	return ret