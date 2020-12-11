import re

not_numeric = re.compile(r"[^\d]")
ops = {'+': (lambda op1, op2: int(op1) + int(op2)),
       '-': (lambda op1, op2: int(op1) - int(op2))}


def pad_left(str, padlength=4):
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
        r2_item = operator + (" " * (longest_op+1-len(op2))) + op2
        row2 = row2 + (r2_item if idx == 0 else pad_left(r2_item))
        r3_item = "-" * len(r2_item)
        row3 = row3 + (r3_item if idx == 0 else pad_left(r3_item))
        r1_item = pad_left(op1, len(r3_item)-len(op1))
        row1 = row1 + (r1_item if idx == 0 else pad_left(r1_item))

        # optional solve
        if(solve):
            operation_func = ops[operator]
            result = str(operation_func(op1, op2))
            result = pad_left(result, len(r3_item)-len(result))
            solution_row = solution_row + \
                (result if idx == 0 else pad_left(result))
            arranged_problems = "\n".join([row1, row2, row3, solution_row])
        else:
            arranged_problems = "\n".join([row1, row2, row3])
    return arranged_problems
