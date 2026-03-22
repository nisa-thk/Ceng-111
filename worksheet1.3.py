user_input = input("Enter a number:")
try:
    number = int(user_input)
    print("Result: ", number*2)
except ValueError:
    print("WARNING!, Please enter a valid whole number")
print("------------EX:2----------------")

numbers = [3, -2, 5, 8, -7, 11, 0, 9]
count = 0
for num in numbers:
    if(num == 0):
        break
    if(num < 0):
        continue
    if(num % 2 != 0):
        count +=1
print("The number of positive odd integers: ", count)
print("--------------EX: 3---------------")

record = "Ada, 10, x, 7, -2"
tokens = [t.strip() for t in record.split(",")]

scores = []
for t in tokens:
    try:
        num = int(t)
    except ValueError:
        continue  # invalid token
    if num < 0:
        continue  # skip the negatives
    scores.append(num)

print("The valid scores:", scores)