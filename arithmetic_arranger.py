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
        (op1, operator, op2) = problem.split(" ")
        # Error handling
        if not_numeric.search(op1) or not_numeric.search(op2):
            return "Error: Numbers must only contain digits."
        if len(op1) > 4 or len(op2) > 4:
            return "Error: Numbers cannot be more than four digits."
        if operator not in allowed_ops:
            return "Error: Operator must be '" + ("' or '".join(allowed_ops)) + "'."

        longest_op = max(len(op1), len(op2))
        pad = ((lambda s: s) if idx == 0 else (lambda s: pad_left(s)))
        r2_item = operator + (" " * (longest_op+1-len(op2))) + op2
        row2 = row2 + pad(r2_item)
        r3_item = "-" * len(r2_item)
        row3 = row3 + pad(r3_item)
        r1_item = pad_left(op1, len(r3_item)-len(op1))
        row1 = row1 + pad(r1_item)

        # optional solve
        if solve:
            operation_func = ops[operator]
            result = str(operation_func(op1, op2))
            result = pad_left(result, len(r3_item)-len(result))
            solution_row = solution_row + pad(result)

    arranged_problems = [row1, row2, row3]
    if solve:
        arranged_problems.append(solution_row)

    return "\n".join(arranged_problems)
