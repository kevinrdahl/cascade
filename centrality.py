import random
import sys

def degree(network):
	ret = []
	for node in network:
		ret.append((node['id'], len(node['friends'])))
	return ret
	
def betweenness(network):
	print '\nComputing network betweenness...'

	ret = [0 for node in network]
	netlen = len(network)
	
	for node in network:
		sys.stdout.write('\r  ' + str(node['id']) + ' / ' + str(netlen) + ' (' + str(100*node['id']/netlen) + '%)')
		sys.stdout.flush()
		#BFS
		layers = [ { node['id']:{'parents':[], 'flow':0, 'seen':False}} ]
		layerNum = 1
		seen = [False for n in network]
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
	print '\nComplete!'
	return ret
					
#assumes that the graph is connected
def closeness(network):
	print '\nComputing network closeness...'
	
	ret = [0 for node in network]
	netlen = len(network)
	
	for node in network:
		sys.stdout.write('\r  ' + str(node['id']) + ' / ' + str(netlen) + ' (' + str(100*node['id']/netlen) + '%)')
		sys.stdout.flush()
		depth = 0
		prevLayer = {node['id']:0} #stupid but appears to perform better
		nextLayer = {}
		seen = [False for n in network]
		
		seen[node['id']] = True
		
		while len(prevLayer) > 0:
			depth += 1
			for node2 in prevLayer:
				for friend in network[node2]['friends']:
					if not seen[friend] and friend not in nextLayer:
						seen[friend] = True
						nextLayer[friend] = 0
						ret[node['id']] += depth
						#print node['id']
			prevLayer = nextLayer
			nextLayer = {}
			
	num = len(network)-1
	for i in range(len(ret)):
		ret[i] = (i, num / float(ret[i]))
	print '\nComplete!'
	return ret
	
#go full retard as a baseline
def rand(network):
	random.seed()
	return [(i,random.random()) for i in range(len(network))]
