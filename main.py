import sys
import io

import cascade

f = open(sys.argv[1], 'r');

network = {}

print 'LOADING...'

for edge in f:
	nodes = edge.split()
	for i in range(len(nodes)):
		node = int(nodes[i])
		if node not in network:
			network[node] = {'id':node, 'friends':[]}
			if len(network) % 250 == 0:
				print '   ' + str(len(network))
		network[node]['friends'].append(int(nodes[(i+1)%2]))
	
f.close()

nodeList = []
for node in network:
	nodeList.append(network[node])
network = nodeList
del nodeList

print 'LOADED'

cascade.tryCascade(network, range(100,500))
