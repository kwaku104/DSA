def capitalizeString(s):
    return ' '.join([word.capitalize() for word in s.strip().split()])


print(capitalizeString("hello    world"))
