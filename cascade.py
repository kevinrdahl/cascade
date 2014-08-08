def tryCascade(network, adopters):
	neighbours = []
	rounds = 0

	for i in range(len(network)):
		network[i]['adopted'] = False
		
	# while there are new adopters
	while len(adopters) > 0:
		rounds += 1
	
		# make this change first to prevent including adopters as neighbours
		for i in adopters:
			network[i]['adopted'] = True
		
		# add each neighbour of new adopters to neighbours
		for i in adopters:
			for j in network[i]['friends']:
				if j not in neighbours and not network[j]['adopted']:
					neighbours.append(j)
					
		adopters[:] = []
					
		# determine whether each of these neighbours would adopt
		for i in neighbours:
			if i in adopters:
				continue
		
			node = network[i]
			numAdopted = 0
			for j in node['friends']:
				if network[j]['adopted']:
					numAdopted += 1
			if (float(numAdopted)/len(node['friends'])) > node['threshold']:
				adopters.append(i)
				
		neighbours[:] = []
		
	numAdopters = 0
	for i in range(len(network)):
		if (network[i]['adopted']):
			numAdopters += 1
			
	#print (str(numAdopters) + ' / ' + str(len(network)) + ' adopters in ' + str(rounds) + ' rounds')
	return (numAdopters, rounds);
	
# centralities = [(id, value)*]	
def selectTopN(network, budget, centralities, useThresh):
	vals = []
	for pair in centralities:
		if (useThresh):
			t = network[pair[0]]['threshold']
		else:
			t = 1.0
		vals.append((pair[0], float(t)*pair[1]))
	vals.sort(key=val, reverse=True)
	adopters = []
	for i in range(budget):
		adopters.append(vals[i][0])
	return adopters
	
def val(iVal):
	return iVal[1]
