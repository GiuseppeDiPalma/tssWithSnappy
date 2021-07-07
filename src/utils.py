
def normalize_dataset(path):
	io = open(path, "r+")
	original = [int(word) for word in io.read().split()]
	io.close()
	values = list(set(original.copy()))
	values.sort()
	mapping = dict()
	for i in range(1, len(values)+1, 1):
	    mapping[values[i-1]] = i
	
	out = open("resources/normalized.txt", "w+")
	phase = 0
	count = 1
	for value in original:
		out.write(str(mapping[value]))
		if count == len(original):
			continue
		if phase == 0:
			out.write("\t")
		else:
			out.write("\n")
		phase = (phase + 1) % 2
		count += 1
	out.close()
	return "resources/normalized.txt"