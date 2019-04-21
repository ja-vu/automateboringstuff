import re

phoneNumRegex = re.compile(r'(\d\d\d)-(\d\d\d-\d\d\d\d)')
mo = phoneNumRegex.search('My number is 451-233-2223')
print(mo.group(1))
print(mo.group(2))


phoneNumRegex1 = re.compile(r'\(\d\d\d\) \d\d\d-\d\d\d\d')
mo1 = phoneNumRegex1.search('My number is (451) 233-2223')
print(mo1.group())

batRegex = re.compile(r'Bat(man|mobile|copter|bat)')
mo2 = batRegex.search('Batmotorcycle lost a wheel')
print(mo2.group())

