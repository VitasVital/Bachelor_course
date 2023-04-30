def shaker(data):
	up = range(len(data) - 1)
	while True:
		for indices in (up, reversed(up)):
			swapped = False
			for i in indices:
				if data[i] > data[i+1]:
					data[i], data[i+1] =  data[i+1], data[i]
					swapped = True
			if not swapped:
				return data