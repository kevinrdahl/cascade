def select(people, numAdopters):

	people.sort(key=degree)

	return people[-numAdopters:]

def degree(person):

	return len(person['friends'])