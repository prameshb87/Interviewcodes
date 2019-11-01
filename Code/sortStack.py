"""
Given a stack sort it such that the min element is at the top. You can only use an additional stack.
"""

# stack1 = [5, 10, 15, 1, 3, 9, 4]
# stack1 = []
# stack1 = [-1, 0, 0, 2, -3]
# stack1 = [1, 1]
# stack1 = [1,2]
# stack1 = [2,1]
stack1 = [2, 110, 29, 80, 11]
stack2 = []

print([n for n in stack1])

def sort_stack(input_stack, temp_stack):
    temp = 0
    if len(input_stack) == 0:
      return []
    while len(input_stack) > 0:
        if len(temp_stack) < 1:
            temp_stack.append(input_stack.pop())
            continue
        if input_stack[-1] < temp_stack[-1]:
            temp = input_stack.pop()
            count = 0
            while len(temp_stack) > 0 and temp <= temp_stack[-1]:
                input_stack.append(temp_stack.pop())
                count += 1
            temp_stack.append(temp)
            for c in range(count):
                temp_stack.append(input_stack.pop())
        else:
            temp_stack.append(input_stack.pop())
        continue
    while len(temp_stack) > 0:
        input_stack.append(temp_stack.pop())
    return input_stack

print([n for n in sort_stack(stack1, stack2)])
