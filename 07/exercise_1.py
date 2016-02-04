in_file = raw_input("Enter a file name: ")
fh = open(in_file, 'r')
for line in fh:
    print line.upper().rstrip()
