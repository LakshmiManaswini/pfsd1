import re
str1="BTS (Korean: 방탄소년단; RR: Bangtan Sonyeondan), also known as the Bangtan boys,"\
     "is a South Korean boy band that was formed in 2010 and debuted in 2013 under Big Hit Entertainment.,"\
     ". The septet—consisting of members Jin, Suga, J-Hope, RM, Jimin, V, and Jungkook—co-writes and co-produces much of their own output."\

matches1=re.findall("Jin",str1)
print(matches1)
matches2=re.search("V",str1)
print(match2)