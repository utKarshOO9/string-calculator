import logging
import re

DELIMITER_REGEX = re.compile(r"//(\[)?\S+(\])?\n")

logger = logging.getLogger(__file__)

class NegativeNumberError(Exception):
    pass


def add(numbers: str) -> int:
    if numbers.strip() == "":
        return 0

    delimiter = "\n"
    match = DELIMITER_REGEX.search(numbers)

    if match is not None:
        numbers = DELIMITER_REGEX.sub("", numbers)
        delimiter = match.group().replace("//", "").strip()
        logger.info(f"delimiter identified as : {delimiter}")


    result = 0
    numbers = numbers.replace(delimiter, ",")
    numbers = numbers.split(",")

    negative_number = []
    for i in numbers:
        if i.strip() == "":
            continue
        int_val = int(i)

        # if negative number should not process forward
        if int_val < 0:
            negative_number.append(i)
            continue

        if int_val > 1000:
            continue

        result += int_val

    if len(negative_number) > 0:
        raise NegativeNumberError(f"negatives not allowed: numbers({','.join(negative_number)})")

    logger.debug(f"addition for numbers: {numbers} result: {result}")
    return result
