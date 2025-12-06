file_name = input("Enter the file path: ") #for .txt files
file = open(file_name, 'r')
data = file.read()
file.close()
data = data.strip()

invalids = 0

def is_invalid_id(num: int) -> bool:
    s = str(num)
    n = len(s)
    if n % 2 != 0:
        return False
    half = n // 2
    return s[:half] == s[half:]

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