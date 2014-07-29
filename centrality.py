def degree(network):
	ret = []
	for node in network:
		ret.append((node['id'], len(node['friends'])))
	return ret
	
def betweenness(network):
	print '\nComputing network betweenness (this may take some time)...'

	ret = [0 for node in network]
	
	for node in network:
		if node['id'] % 100 == 0:
			print '  ' + str(node['id']) + ' / ' + str(len(network))
		#BFS
		layers = [ { node['id']:{'parents':[], 'flow':0, 'seen':False}} ]
		layerNum = 1
		seen = [False for node in network]
		seen[node['id']] = True
		
		while True:
			prevLayer = layers[layerNum-1]
			if len(prevLayer) == 0:
				break
			layer = {}
			for node2 in prevLayer:
				seen[node2] = True
			for node2 in prevLayer:
				for friend in network[node2]['friends']:
					if seen[friend]:
						continue
					if friend not in layer:
						layer[friend] = {'parents':[], 'flow':0, 'seen':False}
					layer[friend]['parents'].append(node2)
			layers.append(layer)
			layerNum += 1
					
		#propagate flow upward
		i = len(layers)-1
		
		while i > 0:
			layer = layers[i]
			for node2 in layer:
				ret[node2] += layer[node2]['flow']
				flow = float(1 + layer[node2]['flow']) / len(layer[node2]['parents'])
				for parent in layer[node2]['parents']:
					layers[i-1][parent]['flow'] += flow
			i -= 1
			
	for i in range(len(ret)):
		ret[i] = (i, ret[i])
	return ret
					
