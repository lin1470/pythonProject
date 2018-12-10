# coding:UTF-8
#废话
import re

# pattern = re.compile(r'\d+')
# print pattern.findall('one1two2three3four4')  # return a result with a list
# for m in re.finditer(pattern,'one1two2three3four4'):
#     print m.group(),  # use a common to avoid to switch a new line

string = 'aa<div>test1</div>bb<div>test2</div>cc '
regex1 = '<div>.*</div>'
regex2 = '<div>.*?</div>'
r1 = re.compile(regex1)
r2 = re.compile(regex2)
print r1.search(string).group()
print r2.search(string).group()
regex3 = '<div>.*</div>bb'
regex4 = '<div>.*?</div>cc'
r3 = re.compile(regex3)
r4 = re.compile(regex4)
print r3.search(string).group()
print r4.search(string).group()