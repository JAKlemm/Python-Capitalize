def capitalize(str):
    str = input('Enter a string: ')
    beginning = True
    result = ''

    for i in str:
        if i.isalpha() and beginning:
            result += i.upper()
            beginning = False
        elif i=='.' or i=='?' or i=='!':
            result += i
            beginning = True
        else:
            result += i

    return result

print(capitalize(str))