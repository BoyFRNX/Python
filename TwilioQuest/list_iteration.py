import sys

leaders = list(sys.argv[1:])

count = 0

for leader in leaders:
    count += 1
    print(f"{count}. {leader}")
