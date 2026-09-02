

import keyword


print(keyword.kwlist)
print(len(keyword.kwlist))

print(keyword.iskeyword("if"))
print(keyword.iskeyword("hello"))
print(keyword.iskeyword("for"))
print(keyword.iskeyword("None"))

status="Pass"
is_updated=True
print(type(status))
print(type(is_updated))

print(isinstance(status,str))