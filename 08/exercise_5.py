import os.path

in_file = os.path.join('..', '07', 'mbox.txt')
from_count = 0

fh = open(in_file, 'r')
for line in fh:
    if line.startswith('From '):
        split_line = line.split()
        if len(split_line) > 1:
            from_count += 1
            print split_line[1]

print 'There were {} lines in the file {} with From as the first word.'.format(from_count, in_file)
