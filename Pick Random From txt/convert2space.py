import sys
import random

src = sys.argv[1]
dst = sys.argv[2]

f = open(src)
tab_content = f.read()
f.close()

space_content = tab_content.replace("\t", " ")
space_content = space_content.replace("\n", " ")

f = open(dst, 'w')
f.write(space_content)
f.close()