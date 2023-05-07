"""
'Hi My name is Andrei' should be reversed to
'ierdnA si emaN iH '
"""

def reverseStr(_str):
    if not _str or type(_str) != str or len(_str) < 2:
        return "Something went wrong."
    strArr = []
    for i in reversed(_str):
        strArr.append(i)
    # strArr.reverse()
    return "".join(strArr)
    # print(strArr)
    # return str(strArr.reverse())


print(reverseStr("Hi my name is Kwaku"))