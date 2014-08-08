import random

def uniform(network):
	random.seed()
	return [random.random() for i in range(len(network))]

def normal(network, mean, sigma):
	random.seed()
	ret = []
	for i in range(len(network)):
		t = -1
		while (t < 0 or t > 1):
			t = random.normalvariate(mean, sigma)
		ret.append(t)
	return ret

def longtail(network, power):
	return [powerlaw(power) for i in range(len(network))]

# got this formula from http://arxiv.org/abs/1010.2265
# http://stats.stackexchange.com/questions/10900/long-tailed-distributions-for-generating-random-numbers-with-parameters-to-contr
def powerlaw(power):
	random.seed()
	rand = random.random()
	ret = rand**((power/2.0)*(rand**2))
	return ret
