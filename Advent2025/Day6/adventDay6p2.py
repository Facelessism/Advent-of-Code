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
            block_cols = [row[start:col] for row in data]
            operator_col = block_cols[-1]
            op = operator_col.strip()
            numbers = []
            for c in reversed(range(col - start)):
                digits = [block_cols[r][c] for r in range(len(block_cols)-1)]
                num_str = ''.join(d for d in digits if d != " ")
                if num_str:
                    numbers.append(int(num_str))
            if op == "+":
                total += sum(numbers)
            else:
                res = 1
                for n in numbers:
                    res *= n
                total += res
            start = None

print(total)
#day6p2