import random

def uniform(network, min, max):
	random.seed()
	return [(i,random.uniform(max, min)) for i in range(len(network))]

def normal(network, mean, sigma):
	random.seed()
	return [(i,random.normalvariate(mean, sigma)) for i in range(len(network))]

def longtail(network, min, max, power):
	return [(i,powerlaw(min, max, power)) for i in range(len(network))]

# got this formula from wolfram mathworld http://mathworld.wolfram.com/RandomNumber.html
# x = ret, x0 = min, x1 = max, y = rand, n = power
def powerlaw(min, max, power):
	random.seed()
	rand = random.uniform(min, max)
	ret = ((max**(power+1) - min**(power+1))*rand + min**(power+1))**(1/(power+1))
	return ret