rules = [
    ("(A . B)'", "A' + B'"),
    ("(A + B)'", "A' . B'"),
    ("(A1 . A2 . A3 ... An)'", "A1' + A2' + ... + An'"),
    ("(A1 + A2 + ... + An)'", "A1' . A2' . ... . An'"),
    ("A.B + A'.C", "(A + C) . (A' + B)"),
    ("A.(B + C)", "A.B + A.C"),
    ("A.B + A.C", "A.(B + C)"),
    ("A . 0", "0"),
    ("A + 1", "1"),
    ("A . 1", "A"),
    ("A + 0", "A"),
    ("A + A", "A"),
    ("A . A", "A"),
    ("A + A'", "1"),
    ("A . A'", "0"),
    ("((A)')'", "A"),
    ("A + B", "B + A"),
    ("A.B", "B.A"),
    ("A + (B + C)", "(A + B) + C"),
    ("A . (B . C)", "(A . B) . C"),
    ("A + A.B", "A"),
    ("A . (A + B)", "A"),
    ("A + A' . B", "A + B"),
    ("A . (A' + B)", "A . B")
]

expression = "A.B + B.C' + A.C"
target_expression = "A.C + B.C'"

def apply_rule(expression, rule):
    lhs, rhs = rule
    if lhs in expression:
        return expression.replace(lhs, rhs)
    return None

print("Starting with expression:", expression)
steps = [expression]

while expression != target_expression:
    for rule in rules:
        transformed = apply_rule(expression, rule)
        if transformed and transformed not in steps:
            expression = transformed
            steps.append(expression)
            print("Applied rule:", rule)
            print("Transformed expression:", expression)
            break
    else:
        print("No further transformation possible.")
        break

print("\nFinal expression:", expression)
print("\nTransformation steps:")
for i, step in enumerate(steps):
    print(f"Step {i}: {step}")
