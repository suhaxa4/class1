def de_morgan(expr):
    return expr.replace("(A . B)'", "A' + B'")

def de_morgan2(expr):
    return expr.replace("(A + B)'", "A' . B'")

def de_morgan3(expr):
    return expr.replace("(A1 . A2 . A3 ... An)'", "A1' + A2' + ... + An'")

def de_morgan4(expr):
    return expr.replace("(A1 + A2 + ... + An)'", "A1' . A2' . A3' ... An'")

def transposition(expr):
    return expr.replace("A.B + A'.C", "(A + C) . (A' + B)")

def duality(expr):
    if "A.(B+C)" in expr:
        expr = expr.replace("A.(B+C)", "A+(B.C)")
        expr = expr.replace("A+(B.C)", "(A+B).(A+C)")
    return expr

def simplify(expr):
    rules = {
        "A.0": "0",
        "A + 1": "1",
        "A.1": "A",
        "A + 0": "A",
        "A + A": "A",
        "A.A": "A",
        "A + A'": "1",
        "A.A'": "0",
        "((A)')'": "A",
        "A + B": "B + A",
        "A.B": "B.A",
        "A+(B+C)": "(A+B)+C",
        "A.(B.C)": "(A.B).C",
        "A.(B+C)": "(A.B)+(A.C)",
        "A.(A+B)": "A",
        "A + A.B": "A",
        "A+ A'.B": "A+B",
        "A.(A' + B)": "A.B"
    }
    for rule, replacement in rules.items():
        if rule in expr:
            expr = expr.replace(rule, replacement)
    return expr

def apply_rules(expr):
    expr = simplify(expr)
    expr = de_morgan(expr)
    expr = de_morgan2(expr)
    expr = de_morgan3(expr)
    expr = de_morgan4(expr)
    expr = duality(expr)
    expr = transposition(expr)
    return simplify(expr)

def prove_equivalence(lhs, rhs):
    steps = [lhs]
    while lhs != rhs:
        new_expr = apply_rules(lhs)
        if new_expr == lhs: 
            break
        lhs = new_expr
        steps.append(lhs)
    
    return lhs == rhs, steps


lhs = "A⋅(A+B)"
rhs = "A"

result, steps = prove_equivalence(lhs, rhs)

print("Proved" if result else "Not Proved")
print("Steps:")
for i, step in enumerate(steps, 1):
    print(f"Step {i}: {step}")



