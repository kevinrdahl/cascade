import sys
import io

import cascade

f = open(sys.argv[1], 'r');

network = {}

for edge in f:
	nodes = edge.split()
	for i in range(len(nodes)):
		node = int(nodes[i])
		if node not in network:
			network[node] = {'friends':[]}
		network[node]['friends'].append(int(nodes[(i+1)%2]))
	
f.close()

print 'LOADED!'

cascade.tryCascade(network, [1,2,3,4,5])
