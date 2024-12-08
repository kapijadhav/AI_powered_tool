def analyze_code(code):
    issues = []
    suggestions = []

    # Check for 'len()' inside 'for' loop
    if 'for i in range' in code and 'len(' in code:
        issues.append("Inefficient loop: Using len() inside for loop.")
        suggestions.append("Avoid using len() inside a loop. Store it in a variable before the loop.")

    # Check for infinite loop 'while True'
    if 'while True' in code:
        issues.append("Infinite loop detected.")
        suggestions.append("Ensure 'while True' has a condition to break or limit iterations.")

    # Add more checks for other performance bottlenecks
    if 'for i in range(10000000)' in code:
        issues.append("Potentially expensive range size.")
        suggestions.append("Consider using a generator or reducing the range size.")

    return {'issues': issues, 'suggestions': suggestions}
