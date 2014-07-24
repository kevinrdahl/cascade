def select(people, budget):

	people.sort(key=degree)
	ret = []
	for person in people[-budget:]:
		ret.append(person['id'])

	return ret

def degree(person):

	return len(person['friends'])