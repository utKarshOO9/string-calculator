
def add(numbers: str) -> int:
    if numbers.strip() == "":
        return 0
    result = 0
    numbers = numbers.split(',')
    for i in numbers:
        if i.strip() == "":
            continue
        result += int(i)
    return result