print("Enter rotations (one per line) & leave a blank line to end:\n")

rotations = []
while True:
    line = input().strip()
    if line == "":
        break
    rotations.append(line)

def new_pass(input_list: list[str]) -> int:
    zero_count = 0
    current_value = 50
    for string in input_list:
        dir, value = string[0], int(string[1:])
        step = -1 if dir == "L" else 1
        for _ in range(value):
            current_value = (current_value + step) % 100
            if current_value == 0:
                zero_count += 1
    return zero_count

password = new_pass(rotations)
print("\nPassword is:", password)
