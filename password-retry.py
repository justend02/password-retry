password = 'a123456'
i = 3
while i > 0:
	pwd = input('please enter your password: ')
	if pwd ==password:
		print('you are right')
		break
	else:
		i = i - 1
		print('you are wrong', i, 'times' )

