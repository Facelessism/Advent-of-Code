file_name = input("Enter the file path: ")  #for .txt files
file = open(file_name, 'r')
data = file.read()
file.close()
data = data.strip()

invalids = 0

def is_invalid_id(num: int) -> bool:
    s = str(num)
    n = len(s)
    if n < 2:
        return False
    for l in range(1, n//2 + 1 ):
        if n % l == 0:
            sub = s[:l]
            if sub * (n // l) == s:
                return True
    return False

def sum_invalid_ids(ranges: str) -> int:
    total = 0
    for r in ranges.split(','):
        start, end = map(int, r.split('-'))
        for num in range(start, end + 1):
            if is_invalid_id(num):
                total += num
    return total

result = sum_invalid_ids(data)
print("Sum of all invalid IDs:", result)