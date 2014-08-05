import sys
import io

import cascade
import centrality
import distribution

if (len(sys.argv) != 5):
	print 'python main.py <network file> <DEG/BTWN/CLS> <UNIFORM/NORMAL/LONGTAIL> <budget>'
	quit()

f = open(sys.argv[1], 'r')
method = sys.argv[2]
distro = sys.argv[3]
budget = int(sys.argv[4])

network = {}

print 'Loading Network...'

for edge in f:
	nodes = edge.split()
	for i in range(len(nodes)):
		node = int(nodes[i])
		if node not in network:
			network[node] = {'id':node, 'friends':[]}
			sys.stdout.write('\r  ' + str(len(network)) + ' nodes')
			sys.stdout.flush()
		network[node]['friends'].append(int(nodes[(i+1)%2]))

f.close()

# do distribution somewhere here

if distro == 'UNIFORM':
	thresholds = distribution.uniform(network, 0, 1)
elif method == 'NORMAL':
	thresholds = distribution.normal(network, 0.5, 1)
elif method == 'LONGTAIL':
	thresholds = distribution.longtail(network, 0, 1, 2)
else:
	print 'Distribution should be UNIFORM, NORMAL, or LONGTAIL'
	quit()

# use network for centrality param
nodeList = []
for node in network:
	nodeList.append(network[node])
network = nodeList
del nodeList

print '\nComplete!'

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

print '\nInitial Adopters:'
print adopters

cascade.tryCascade(network, adopters)
