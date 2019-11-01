"""
Given a string containing digits 2-9 inclusive, return all possible letter
combinations that the number could represent.
A mapping of digits to numbers is similar to telephone buttons
eg input - '23'
output = ['ad', 'ae', 'af', 'bd', 'be', 'bf', 'cd', 'ce', 'cf']
"""
def solution(digits):
    """
    solution is to loop over each digit's mapping letters and keep adding to a
    string. To prevent having to write explicit for loops a recursive
    approach is used.
    Iterate over the first digit's mapping string, and call the recursive
    function on the next digit's mapping string. Recursion will handle
    further digits. We stop if a string with the same number of digits has been
    produced and then continue on to the next iteration of the earliest loop.
    """
    mapping = [
        '',
        '',
        'abc',
        'def',
        'ghi',
        'jkl',
        'mno',
        'pqrs',
        'tuv',
        'wxyz'
    ]
    result = []
    index = 0
    current = ''
    get_letter_combinations(digits, mapping, current, index, result)
    return result

def get_letter_combinations(digits, mapping, current, index, result):
    if index == len(digits): # current string has all possible characters for the given digits combinations
        result.append(current)
        return
    for c in mapping[int(digits[index])]:
        get_letter_combinations(digits, mapping, current + c, index + 1, result)

digits = '23'
print(solution(digits))
