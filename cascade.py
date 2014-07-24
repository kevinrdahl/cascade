def tryCascade(network, adopters):
	neighbours = []

	for i in range(len(network)):
		network[i]['adopted'] = False
		network[i]['threshold'] = 0.3 #temporary
		
	# while there are new adopters
	while len(adopters) > 0:
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
			
	print (str(numAdopters) + ' adopters of ' + str(len(network)) + ' people')
