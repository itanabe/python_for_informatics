in_file = raw_input("Enter a file name: ")
header = "X-DSPAM-Confidence:"
spam_count = 0
spam_confidence_sum = 0.0

fh = open(in_file, 'r')
for line in fh:
    if line.startswith(header):
        str_float = line[len(header):].strip()
        spam_count += 1
        spam_confidence_sum += float(str_float)

print "Average spam confidence: " + str(spam_confidence_sum / spam_count)