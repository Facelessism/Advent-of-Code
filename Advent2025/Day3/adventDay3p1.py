def pick_n(s: str, n: int) -> int:
    s = s.strip()
    if len(s) < n or n == 0:
        return 0

    out = []
    start = 0

    while len(out) < n:
        need = n - len(out)
        skip = len(s) - start - need
        end = start + skip

        best = start
        for i in range(start, end + 1):
            if s[i] > s[best]:
                best = i

        out.append(s[best])
        start = best + 1

    return int("".join(out))

def main():
    print("Enter the numbers & press ENTER to finish):")
    total = 0
    
    while True:
        ln = input().strip()
        if not ln:
            break
        total += pick_n(ln, 2)  #Change the value from 2 to 12 here if running part2 instead of part1

    print("\nTotal output joltage:", total)

main()
