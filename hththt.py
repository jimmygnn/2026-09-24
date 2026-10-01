count_text = input("請輸入數量：")
print(type(count_text))  # 輸入 3，仍得到 <class 'str'>
count = int(count_text)  # 把字串轉為整數
print(count + 1)  # 4