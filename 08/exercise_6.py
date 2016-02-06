numbers = list()

while True:
    num = raw_input("Enter a number: ").strip()
    if num == 'done': break
    if len(num) == 0: continue
    try:
        num = float(num)
    except:
        print num + " is not a number."
        continue

    numbers.append(num)

if len(numbers):
    print 'Maximum: {}'.format(max(numbers))
    print 'Minimum: {}'.format(min(numbers))
else:
    print 'Number list is empty.'