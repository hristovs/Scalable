import string
import locale
writefile = open('sortedrockyou.txt', 'w')
with open('rockyou', encoding = "ISO-8859-1") as f:
    lines = f.readlines()

for i in lines:
	if len(i) > 4 and len(i) < 9:
		if i.islower():		
			writefile.write(i)
