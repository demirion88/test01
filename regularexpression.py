import re
# r=re.compile("a.c")

# a=r.search("kkk")
# print(a)
#
# a=r.search("abc")
# print(a)

# r=re.compile("ab?c")
# r.search("abbc")
#
# a=r.search("abc")
# print(a)
#
# b=r.search("ac")
# print(b)

# r=re.compile("ab*c")
# a=r.search("ac")
#
# b=r.search("abc")
# print(b)
# c=r.search("abbbc")
# print(c)

# r=re.compile("ab+c")
# a=r.search("ac")
# print(a)
# b=r.search("abc")
# print(b)


# text="Regular expression : A regular expression, regex or regexp[1] (sometimes called a rational expression)[2][3] is, in theoretical computer science and formal language theory, a sequence of characters that define a search pattern."
# print(re.sub('[^a-zA-Z]',' ',text))

text = """100 John    PROF
101 James   STUD
102 Mac   STUD"""

a=re.split('\s+', text)
print(a)