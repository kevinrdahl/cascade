import sys
import io

import cascade
import centrality

if (len(sys.argv) != 3):
	print 'python main.py <network file> <budget>'
	quit()

f = open(sys.argv[1], 'r');
budget = int(sys.argv[2])

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

print 'LOADED (' + str(len(network)) + ')'

adopters = cascade.selectTopN(budget, centrality.degree(network))

cascade.tryCascade(network, adopters)
