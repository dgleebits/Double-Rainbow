import sys, md5

f = open(sys.argv[1])
obj = md5.new()

for line in f:
  if line[-1:] == '\n':
		text = line[:-1]
		obj.update(text),
		print text + '|' + obj.hexdigest()

f.close()