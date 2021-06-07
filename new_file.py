print('Alphabetic Pattern')
rows=5
chara=65
for i in range(rows):
	for j in range(i):
		print(chr(chara),end=' ')
		chara+=1
	print(' ')