import re

not_numeric = re.compile(r"[^\d]")
ops = {'+': (lambda op1, op2: int(op1) + int(op2)),
       '-': (lambda op1, op2: int(op1) - int(op2))}


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    row1, row2, row3, solution_row = [], [], ['----']*len(problems), []

    allowed_ops = ops.keys()
    for problem in problems:
        # Error handling
        (op1, operator, op2) = problem.split(" ")
        if not_numeric.search(op1) or not_numeric.search(op2):
            return "Error: Numbers must only contain digits."
        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in allowed_ops:
            return "Error: Operator must be '" + ("' or '".join(allowed_ops)) + "'."

        row1.append(op1)
        row2.append(operator + ' ' + op1)

        # optional solve
        if(solve):
            operation_func = ops[operator]
            solution_row.append(operation_func(op1, op2))

    return arranged_problems
