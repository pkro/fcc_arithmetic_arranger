import re

not_numeric = re.compile(r"[^\d]")
ops = {'+': (lambda op1, op2: int(op1) + int(op2)),
       '-': (lambda op1, op2: int(op1) - int(op2))}


def pad_left(str, padlength=5):
    padding = " "*padlength
    return f"{padding}{str}"


def arithmetic_arranger(problems, solve=False):
    if len(problems) > 5:
        return "Error: Too many problems."

    arranged_problems = ""
    row1, row2, row3, solution_row = "", "", "", ""

    allowed_ops = ops.keys()
    for idx, problem in enumerate(problems):
        # Error handling
        (op1, operator, op2) = problem.split(" ")
        if not_numeric.search(op1) or not_numeric.search(op2):
            return "Error: Numbers must only contain digits."
        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in allowed_ops:
            return "Error: Operator must be '" + ("' or '".join(allowed_ops)) + "'."

        longest_op = len(op1) if len(op1) > len(op2) else len(op2)
        r1_item = pad_left(op1, 4-longest_op)
        row1 = row1 + (r1_item if idx == 0 else pad_left(r1_item))
        r2_item = operator + (" " * (4-longest_op+1)) + op2
        row2 = row2 + (r2_item if idx == 0 else pad_left(r2_item))
        r3_item = "-" * len(r2_item)
        row3 = row3 + (r3_item if idx == 0 else pad_left(r3_item))

        # optional solve
        if(solve):
            operation_func = ops[operator]
            result = operation_func(op1, op2)
            solution_row = solution_row + pad_left(str(result))

    arranged_problems = "\n".join([row1, row2, row3, solution_row])
    return arranged_problems
