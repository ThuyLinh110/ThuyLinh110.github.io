import string
text = open("paper.txt",'r',encoding="utf8")
d = dict()
special="/-"
for line in text:
	line = line.strip()
	line = line.lower()
	line = line.translate(line.maketrans(special,"  "))
	line = line.translate(line.maketrans("", "", string.punctuation))
	words = line.split(" ")
	for word in words:
		if word in d:
			d[word] = d[word] + 1
		else:
			d[word] = 1
def most_frequent(list):
    return max(list,key=list.get)
#1
print('word is the most frequent : ',most_frequent(d))
#2
lis =list(set(words))
lis.sort()
print(lis)
#3
for key in list(d.keys()):
	print(key, ":", d[key])
