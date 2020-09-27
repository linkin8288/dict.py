data = []
count = 0 # 計數器
with open('reviews.txt', 'r') as f: # 讀取txt檔案當作f
	for line in f: # 每次讀取都讀取一行，取名為line
		data.append(line) # 將每一行加入空data清單裡面
		# 新的清單放前面，append(line)
		count += 1 
		if count % 100000 == 0: # 每讀100000筆資料印出來，%是求餘數
			print(len(data))

print('檔案讀取玩了，總共有', len(data), '筆資料') # len()是讀取長度

# 計算出現過的次數
wc = {} # word_count
for d in data: # 每一筆d都是字串，一筆留言
	words = d.split(' ') # 用空格分隔字串
	for word in words:
		if word in wc:
			wc[word] += 1 # 字的次數加一
		else:
			wc[word] = 1 # 新增key到字典裏面

for word in wc: # 把每一個key叫出來
	if wc[word] > 900000:
		print(word, wc[word]) # key, 次數

print(wc['Allen']) # 查詢Allen有沒有在字典裏面

while True:
	word = input('請問你想查甚麼字: ')
	print(word, '出現過的次數為:', wc[word])


	
