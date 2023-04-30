def insertion(data):
	for i in range(len(data)):
		j = i - 1
		key = data[i]
		while data[j] > key and j >= 0:
			data[j + 1] = data[j]
			j -= 1
		data[j + 1] = key
	return data