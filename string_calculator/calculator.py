import re

DELIMITER_REGEX = re.compile(r"(//\S\n)")

def add(numbers: str) -> int:
    if numbers.strip() == "":
        return 0
    
    delimiter = "\n"
    match = DELIMITER_REGEX.search(numbers)
    
    if match is not None:
        numbers = DELIMITER_REGEX.sub("", numbers)
        delimiter = match.group(1).replace("//", "").strip()
        
    result = 0
    numbers = numbers.replace(delimiter, ',')
    numbers = numbers.split(',')

    for i in numbers:
        if i.strip() == "":
            continue
        result += int(i)
    
    return result
