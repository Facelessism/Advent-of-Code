current_value = 50
zero_count = 0

print("Enter rotations(one per line) & leave a blank line to end:\n")

while True:
    line = input().strip()
    if line == "":
        break

    dir = line[0]
    num = line[1:]

    if not num.isdigit():
        continue

    value = int(num)

    if dir == "L":
        current_value = (current_value - value) % 100
    elif dir == "R":
        current_value = (current_value + value) % 100

    if current_value == 0:
        zero_count += 1

print("\nPassword is:", zero_count)
