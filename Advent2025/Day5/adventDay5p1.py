file_name = input("Enter the file path: ")  # for .txt files
file = open(file_name, 'r')
data = file.read()
file.close()
data = data.strip().splitlines()


def count_fresh(lines):
    ranges = []
    ids = []
    blank_seen = False

    for line in lines:
        line = line.strip()
        if line == "":
            blank_seen = True
            continue

        if not blank_seen:
            a, b = map(int, line.split("-"))
            ranges.append((a, b))
        else:
            ids.append(int(line))

    if not ranges:
        return 0

    ranges.sort()
    merged = []

    cur_start, cur_end = ranges[0]
    for start, end in ranges[1:]:
        if start <= cur_end + 1:
            cur_end = max(cur_end, end)
        else:
            merged.append((cur_start, cur_end))
            cur_start, cur_end = start, end

    merged.append((cur_start, cur_end))

    fresh_count = 0

    for x in ids:
        for s, e in merged:
            if s <= x <= e:
                fresh_count += 1
                break

    return fresh_count

result = count_fresh(data)
print(result)
