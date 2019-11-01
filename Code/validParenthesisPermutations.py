"""
For a given pair of parenthesis, print all valid permutations. Every left parenthesis
should have a matching and valid right parenthesis
"""
def printPerms(list, left_remaining, right_remaining, str, index, count):
    count+=1
    print(list, left_remaining, right_remaining, str, index, count)
    if left_remaining < 0 or right_remaining < left_remaining:
        return
    if left_remaining == 0 and right_remaining == 0:
        list.append(''.join(str))
    else:
        if index == len(str): # in case str is []
          str.insert(index, '(')
        else:
          str[index] = '('
        printPerms(list, left_remaining - 1, right_remaining, str, index + 1, count)
        if index == len(str):
          str.insert(index, ')')
        else:
          str[index] = ')'
        printPerms(list, left_remaining, right_remaining - 1, str, index + 1, count)


list = []
printPerms(list, 3, 3, [], 0, 0)
print(list)
