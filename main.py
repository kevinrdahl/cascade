import sys
import io

import cascade
import centrality
import distribution

if (len(sys.argv) != 5):
	print '''python main.py 
			<network file>
			<UNIFORM/NORMAL/LONGTAIL> 
			<budgets (comma separated)> 
			<# of trials>'''
	quit()

try:
	f = open(sys.argv[1], 'r')
	distro = sys.argv[2]
	budgets = [int(num) for num in sys.argv[3].split(',')]
	numTrials = int(sys.argv[4])
except:
	print 'Something has gone horribly wrong.'
	quit()

network = {}

print '\nLoading Network...'

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
print '\n'

# use network for centrality param
nodeList = []
for node in network:
	nodeList.append(network[node])
network = nodeList
del nodeList
	
centralities = 	{
				'Degree' : centrality.degree(network),
				'Betweenness' : centrality.betweenness(network),
				'Closeness' : centrality.closeness(network)
				}

hybrid = centrality.hybrid( [centralities[name] for name in centralities] )
centralities['Hybrid'] = hybrid

results = {budget:{method:[] for method in centralities} for budget in budgets}

print ''
for trial in range(numTrials):
	thresholds = []
	if distro == 'UNIFORM':
		thresholds = distribution.uniform(network)
	elif distro == 'NORMAL':
		thresholds = distribution.normal(network)
	elif distro == 'LONGTAIL':
		thresholds = distribution.longtail(network, 20)
	else:
		print '\nDistribution should be UNIFORM, NORMAL, or LONGTAIL'
		quit()
		
	for i in range(len(thresholds)):
		#print 'thresholds[' + str(i) + '] = ' + str(thresholds[i])
		network[i]['threshold'] = thresholds[i]
	
	for i in range(len(budgets)):
		budget = budgets[i]
		methodCount = 0
		for method in centralities:
			methodCount += 1
			sys.stdout.write('\rTrial ' + str(trial+1) + '/' + str(numTrials) + ', ')
			sys.stdout.write('Budget ' + str(i+1) + '/' + str(len(budgets)) + ', ')
			sys.stdout.write('Method ' + str(methodCount) + '/' + str(len(centralities)))
			sys.stdout.flush()
			adopters = cascade.selectTopN(budget, centralities[method])
			results[budget][method].append(cascade.tryCascade(network, adopters)[0])
			
print '\n\n===RESULTS==='
for budget in budgets:
	print '\n' + str(budget) + ' initial adopters:'
	for method in centralities:
		scores = results[budget][method]
		scores.append(float(sum(scores))/len(scores))
		print method + ': ' + str(scores[-1]) + ' / ' + str(len(network))

print '\nComplete!'
