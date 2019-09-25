import sys
import random

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

spt = tab_content.split(' ')

length = len(spt)

f = open(dst, 'w')
i = 0

while i < 20:
	f.write(spt[random.randint(1, length-1)])
	f.write("\n")
	i = i + 1
	print(i)

f.close()