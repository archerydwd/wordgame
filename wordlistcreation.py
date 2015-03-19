allwords = "/usr/share/dict/words"
with open(allwords) as words:
	for line in words:
		if len(line) > 7:
			with open("sourcewords.txt", 'a') as source:
				source.write(line.lower())
		if len(line) > 3:
			with open("validwords.txt", 'a') as valid:
				valid.write(line.lower())
		else:
			pass
