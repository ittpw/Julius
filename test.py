# -*- cording: utf-8 -*-

#音声認識結果テキストファイル読み込み
f = open("text.txt","r")

texts = []
for line in f:
	if line[:10] == "sentence1:":
		texts.append("".join(line[12:-1].split(" ")))

f.close()

#テキストファイル出力
print("\n---------音声認識---------\n", end ='')
for t in texts:
  print(t)

#形態素解析
import MeCab
m = MeCab.Tagger ("-Ochasen")
a = []

print("\n\n---------形態素解析---------\n", end ='')

mtxt = []

for tt in texts:
	mtxt.append(m.parse(tt).split("\n"))
print(mtxt)
print("\n\n\n")
for m in mtxt:
	for mword in m[:-2]:
		wordclass = mword.split("\t")
		if "名詞" in wordclass[3]:
			print(wordclass[0],wordclass[3])

