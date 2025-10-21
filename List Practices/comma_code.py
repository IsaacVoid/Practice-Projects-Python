def comma_and(items):
    if not items:
        return "lista vacía"
    if len(items) == 1:
        return str(items[0])
    if len(items) == 2:
        a, b = items
        return f"{a} and {b}"
    # Oxford comma: coma antes de "and"
    return f"{', '.join(map(str, items[:-1]))}, and {items[-1]}"

spam = ['apples', 'bananas', 'tofu', 'lemons', 'grapes', 'pineapple']
print(comma_and(spam))
