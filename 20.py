def isValid(s):
    stack = []
    dict = {"]":"[", "}":"{", ")":"("}
    for char in s:
        print(char, stack)
        if char in '[{(':
            stack.append(char)
        elif char in ']})':
            if stack == [] or dict[char] != stack.pop(): 
               return False
        else:
            return False
    return stack == []



# isValid('[][{()}][][]')
print(43560**0.5)