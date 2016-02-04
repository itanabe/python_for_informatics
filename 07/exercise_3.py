in_file = raw_input("Enter the file name: ")
magic_phrase = "na na boo boo"

if in_file == magic_phrase:
    print magic_phrase.upper()
    exit()

fh = None
subject_count = 0
lines = " lines"

try:
    fh = open(in_file, 'r')
except:
    print "File cannot be opened: " + in_file
    exit()

for line in fh:
    if line.startswith("Subject:"):
        subject_count += 1

if subject_count == 1:
    lines = " line"

print "There were " + str(subject_count) + lines + " in " + in_file