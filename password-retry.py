password = 'a123456'
i = 3
while True:
	pwd = input('please enter your password: ')
	if pwd ==password:
		print('you are right')
		break
	else:
		i = i - 1
		print('you are wrong', i, 'times' )
		if i == 0:
			break
	
