def readTabforWombo(filename):
	with open(filename) as womboDirections:
		## Saved files with Tabs to make it easier to deal with commas
		reader = csv.DictReader(womboDirections, delimeter='\t')

		for dir in reader:

			if dir['Style'] != 'Done' and len(dir['Summary']) > 0:
				wombo(dir['Summary'], dir['Style'], dir['Genre'])