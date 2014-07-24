def select(people, numAdopters):

	people.sort(key=degree)

	return people[-10]

def degree(person):

	return len(person['friends'])