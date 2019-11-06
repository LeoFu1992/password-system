pwd = '1024'
x = 1
while x < 4:
	password = input('請輸入四位數密碼:')
	if password == pwd:
		print('登入成功')
		break
	elif password != pwd:
		x = x + 1
		print('密碼錯誤，你還有兩次機會')
		password = input('請輸入四位數密碼:')
		if password == pwd:
			print('登入成功')
			break
		elif password != pwd:
			x = x + 1
			print('密碼錯誤，你還有一次機會')
			password = input('請輸入四位數密碼:')
			if password == pwd:
				print('登入成功')
				break
			elif password != pwd:
				x = x + 1
				print('密碼錯誤，你沒有機會了')
				break