a = input('how old are you: ')
c = input('have you ever drove a car: ')
a = int(a)
if a >= 18 and c == 'yeah':
	print('good')
elif a < 18 and c == 'yeah':
	print('you should not have driven a car')
elif a < 18 and c == 'no':
	print('You still have to wait to get a license and drive')
elif a >= 18 and c == 'no':
	print('you should go get a license and drive')
