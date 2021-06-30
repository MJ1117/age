driving = input('請問你有沒有開過車?')
if driving != '有' and driving != '沒有':
	print('麻煩你聽懂我的問題 謝謝!')
	raise SystemExit
age = input('請問你的年齡?')
age = int(age)
if driving == '有':
	if age >= 18:
		print('恭喜你通過測驗了')
	else:
		print('奇怪了 你怎麼會有開過車')
elif driving == '沒有':
	if age >= 18:
		print('你要加油囉!')
	elif age >= 15 and age < 17: 
		print('加油你還有一兩年就可以考駕照囉!')
	else:
		print('先忍耐點騎腳踏車或坐大眾交通工具喔!')
