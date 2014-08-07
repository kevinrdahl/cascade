import random

def uniform(network, min, max):
	random.seed()
	return [random.uniform(max, min) for i in range(len(network))]

def normal(network, mean, sigma):
	random.seed()
	ret = []
	for i in range(len(network)):
		t = -1
		while (t < 0 or t > 1):
			t = random.normalvariate(mean, sigma)
		ret.append(t)
	return ret

def longtail(network, min, max, power):
	return [powerlaw(min, max, power) for i in range(len(network))]

# got this formula from wolfram mathworld http://mathworld.wolfram.com/RandomNumber.html
# x = ret, x0 = min, x1 = max, y = rand, n = power
def powerlaw(min, max, power):
	random.seed()
	rand = random.uniform(min, max)
	ret = ((max**(power+1) - min**(power+1))*rand + min**(power+1))**(1/(power+1))
	return ret
