import random
import sys
import math

def degree(network):
	print 'Computing network degree...'
	ret = []
	netlen = len(network)
	for node in network:
		sys.stdout.write('\r  ' + str(node['id']+1) + ' / ' + str(netlen) + ' (' + str(100*(node['id']+1)/netlen) + '%)')
		sys.stdout.flush()
		ret.append((node['id'], len(node['friends'])))
	print ''
	return ret
	
def betweenness(network):
	print 'Computing network betweenness...'

	ret = [0 for node in network]
	netlen = len(network)
	
	for node in network:
		sys.stdout.write('\r  ' + str(node['id']+1) + ' / ' + str(netlen) + ' (' + str(100*(node['id']+1)/netlen) + '%)')
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
	print ''
	return ret
					
#assumes that the graph is connected
def closeness(network):
	print 'Computing network closeness...'
	
	ret = [0 for node in network]
	netlen = len(network)
	
	for node in network:
		sys.stdout.write('\r  ' + str(node['id']+1) + ' / ' + str(netlen) + ' (' + str(100*(node['id']+1)/netlen) + '%)')
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
	print ''
	return ret
	
#returns highest z-scores from among each centrality
def hybrid(centralities):
	print 'Computing highest z-scores...'
	ret = []
	zscores = []

	for centrality in centralities:
		centrality.sort(key=index) #can't be too careful these days
		z = []
		avg = 0
		for pair in centrality:
			avg += pair[1]
		avg = float(avg) / len(centrality)
		
		var = 0
		for pair in centrality:
			var += (pair[1]-avg)**2
		var = float(var) / len(centrality)
		sd = math.sqrt(var)
		
		for pair in centrality:
			z.append(float(pair[1]-avg)/sd)
		zscores.append(z)
		
	for i in range(len(centralities[0])):
		scores = [z[i] for z in zscores]
		ret.append((i, max(scores)))
	return ret

def index(iVal):
	return iVal[0]
	
#go full retard as a baseline
def rand(network):
	random.seed()
	return [(i,random.random()) for i in range(len(network))]
