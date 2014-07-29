import sys
import io

import cascade
import centrality

if (len(sys.argv) != 4):
	print 'python main.py <network file> <DEG/BTWN/CLS> <budget>'
	quit()

f = open(sys.argv[1], 'r')
method = sys.argv[2]
budget = int(sys.argv[3])

network = {}

print 'LOADING...'

for edge in f:
	nodes = edge.split()
	for i in range(len(nodes)):
		node = int(nodes[i])
		if node not in network:
			network[node] = {'id':node, 'friends':[]}
			if len(network) % 250 == 0:
				print '  ' + str(len(network))
		network[node]['friends'].append(int(nodes[(i+1)%2]))
	
f.close()

# use network for centrality param
nodeList = []
for node in network:
	nodeList.append(network[node])
network = nodeList
del nodeList

print 'LOADED (' + str(len(network)) + ')'

if method == 'DEG':
	centralities = centrality.degree(network)
elif method == 'BTWN':
	centralities = centrality.betweenness(network)
elif method == 'CLS':
	centralities = centrality.closeness(network)
elif method == 'RAND':
	centralities = centrality.rand(network)
else:
	print 'method should be DEG, BTWN, or CLS'
	quit()

adopters = cascade.selectTopN(budget, centralities)

cascade.tryCascade(network, adopters)
