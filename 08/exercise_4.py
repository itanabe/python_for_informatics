in_file = 'romeo.txt'
word_list = list()
fh = open(in_file, 'r')
for line in fh:
    words = line.split()
    for word in words:
        word_normalised = word.lower()
        if word_normalised not in word_list:
            word_list.append(word_normalised)

word_list.sort()
print word_list
