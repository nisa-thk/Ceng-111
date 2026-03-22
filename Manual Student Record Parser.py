records = [
    "Ada, 10, 15, x, 20",
    "Lin, 5, -3, 7, nine",
    "Mert, 12, 18",
    "STOP",
    "Zeynep, 100"
]

summaries = []
errors = []
row_index = 0

while(row_index< len(records)):
    line = records[row_index]

    if(line== "STOP"):
        break
    tokens= []
    current = " "
    char_index= 0
    while char_index < len(line):
        ch = line[char_index]

        if ch == ",":
            tokens.append(current.strip())
            current= " "
        else:
            current += ch
        char_index += 1
    tokens.append(current.strip())
    name = tokens[0]
    scores = []

    for token in tokens[1:]:
        if token == "":
            continue

        try:
            value = int(token)
        except ValueError:
            errors.append((name, token))
            continue

        if value < 0:
            continue

        scores.append(value)

    total = 0
    for score in scores:
        total += score

    if len(scores) == 0:
        level = "No valid scores"
    else:
        average = total / len(scores)

        if average >= 15:
            level = "High"
        elif average >= 8:
            level = "Medium"
        else:
            level = "Low"

    summaries.append((name, tuple(scores), level))
    row_index += 1

print("Summaries:", summaries)
print("Errors:", errors)
