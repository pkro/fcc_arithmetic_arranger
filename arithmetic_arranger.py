def arithmetic_arranger(problems, solve=False):
    arranged_problems = ""
    ops = {'-': (lambda op1, op2: int(op1) - int(op2)),
           '+': (lambda op1, op2: int(op1) + int(op2))}
    for problem in problems:
        (op1, operator, op2) = [x for x in problem.split(" ")]
        operation_func = ops[operator]
        print(operation_func(op1, op2))

        arranged_problems = arranged_problems + problem
        print(problem)
        return arranged_problems
