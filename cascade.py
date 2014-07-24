def tryCascade(network, adopters):
	neighbours = []

	for i in network:
		network[i]['adopted'] = False
		
	while len(adopters) > 0:
		for i in adopters:
			adopters[i]['adopted'] = true
		
		for i in adopters:
			for j in adopters[i]['friends']:
				if not j in neighbours:
					neighbours.append(j)
					
		
