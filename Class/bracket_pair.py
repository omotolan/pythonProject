def bracket_pair_checker(brackets: str) -> bool:
    stack = []
    for bracket in brackets:
        if bracket in '[({':
            stack.append(bracket)
        if bracket in '}])':
            peak = stack[-1]
            if bracket == ')' and peak == '(':
                stack.pop()
            if bracket == ']' and peak == '[':
                stack.pop()
            if bracket == '{' and peak == '}':
                stack.pop()
    return len(stack) == 0
