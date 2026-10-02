 # 設定預設的帳號與密碼（使用字串）
a = 'rgrgrgjrf'
b = 'karins546'

# 讀取使用者輸入（帳號密碼通常含有英文，故不轉成 int）
f = input('請輸入帳號：')
g = input('請輸入密碼：')

# 模擬讀取帳戶餘額
c = 45000

if f == a and g == b:
	print('登入成功', '帳戶餘額：', c)
else:
	print('帳號或密碼錯誤')

