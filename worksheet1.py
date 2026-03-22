rows = [
    "10 4 x 7",
    "3 -2 9",
    "8 y 1",
    "STOP",
    "100 200"
]

valid_rows = []
errors = []

for row_index, row in enumerate(rows):
    if row == "STOP":
        break

    tokens = row.split()

    # Geçerli sayılar
    current_valid = [int(t) for t in tokens if t.isdigit() and int(t) > 0]

    # Hatalı tokenlar
    current_errors = [(row_index, t) for t in tokens if not t.isdigit()]

    valid_rows.append(tuple(current_valid))
    errors.extend(current_errors)

print("Valid rows:", valid_rows)
print("Errors:", errors)
