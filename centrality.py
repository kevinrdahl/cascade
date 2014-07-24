def degree(people, budget):

	people.sort(key=deg)
	ret = []
	for person in people[-budget:]:
		ret.append(person['id'])

	return ret

def deg(person):

	return len(person['friends'])