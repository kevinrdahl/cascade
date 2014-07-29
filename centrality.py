def degree(network):
	ret = []
	for node in network:
		ret.append((node['id'], len(node['friends'])))
	return ret
	
def betweenness(network):
	ret = [0 for node in network]
	
	for node in network:
		#BFS
		layers = [{ [node['id']:{'parents':[], 'flow':0}] }]
		seen = [node['id']]
		
		while True:
			prevLayer = layers[-1]
			if len(prevLayer) == 0:
				break
			layer = {}
			for node2 in prevLayer:
				seen.append(node2)
			for node2 in prevLayer:
				for friend in network[node2]['friends']:
					if friend in seen:
						continue
					if friend not in layer:
						layer[friend] = {'parents':[], 'flow':0}
					layer[friend]['parents'].append(node2)
		layers.append(layer)
					
		#propagate flow upward
		i = len(layers)-1
		while i > 0:
			layer = layers[i]
			for node2 in layer:
				flow = float(1 + layer[node2]['flow']) / len(layer[node2]['parents'])
				for parent in layer[node2]['parents']:
					layer[i-1][parent]['flow'] += flow
					
