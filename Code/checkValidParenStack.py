def is_paren_valid(string):
    is_valid = True
    if len(string) < 1:
        return False
    s = Stack()
    while is_valid:
        for c in string:
            if c in ['{', '[', '(']:
                s.push(c)
            else:
                if s.is_empty():
                    is_valid = False
                else:
                    top = s.peek()
                    if c == '}' and top == '{' or  c == ']' and top == '[' or c == ')' and top == '(':
                        pass
                    else:
                        is_valid = False
        return s.is_empty() and is_valid
