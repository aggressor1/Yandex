from collections import defaultdict
words = defaultdict(list)
for i in sorted([input().lower() for i in range(int(input()))]):
    words[''.join(sorted(i))].append(i)
for i in words:
    print(' '.join(sorted(words[i])))