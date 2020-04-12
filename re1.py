'''正規表現
>tokens
基本文字 .^$*+?|\
括弧 []{}()
最小一致 *? +? ??
繰返し {m} {m,n} {m,n}?
否定 (?!..)

>methods
re.compile(pattern)
re.match(pattern,string)
re.findall(pattern,string)
re.sub(pattern,replace,string)

>特殊シーケンス
\number,\A,\b,\B,\d,\D,\s,\S,\w,\W,\Z

>注意
- match()は、パターンがマッチ対象の文字列全体に一致するものを取得する
では、一致する部分文字列を取得するには？->括弧()
- "(..)*"(0個以上)は、マッチしない一字を読む毎に空文字がマッチする
'''
import re

s0 = "test.txt"
s1 = "test.cpp"
s2 = "ababkebab"
s3 = "..."
s4 = "Today is 2003/03/24."
s5 = "500"
s6 = "trash as an asshole"
s7 = "car and carve"

#works!
p0 = re.compile(r"(ab)*")
p1 = re.compile(r".*\.txt")
p2 = re.compile(r"(\.)*")
p3 = re.compile(r".*\d{4}/\d{2}/\d{2}")
p4 = re.compile(r"^(?!abc).*$")
p5 = re.compile(r".*\d{3}.*")
p6 = re.compile(r"(.?as)")
p7 = re.compile(r"car")
p8 = re.compile(r"")

m = re.findall(p6,s6)
s = re.sub(r"(ab)+?","c",s2)
    
print(m)
