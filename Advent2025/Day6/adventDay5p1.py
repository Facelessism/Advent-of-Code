file_name = input("Enter the file path: ")  # for .txt files
file = open(file_name, 'r')
data = file.read()
file.close()
data = data.strip().splitlines()

width = max(len(line) for line in data)
data = [line.ljust(width) for line in data]

total = 0
start = None

for col in range(width + 1):
    if col < width and any(row[col] != " " for row in data):
        if start is None:
            start = col
    else:
        if start is not None:
            block = [row[start:col].strip() for row in data if row[start:col].strip()]
            op = block[-1]
            nums = list(map(int, block[:-1]))
            total += sum(nums) if op == "+" else eval("*".join(map(str, nums)))
            start = None

print("\ntotal sum is- ",total)
