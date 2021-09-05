password = 'a123456'
i = 3
while i > 0:
	i = i - 1
	pwd = input('please enter your password: ')
	if pwd ==password:
		print('you are right')
		break
	else:
		print('you are wrong')
		if i > 0:
			print('still', i, 'times')
		else:
			print('you are going to lose your account')

