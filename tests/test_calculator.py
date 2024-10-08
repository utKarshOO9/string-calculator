import inspect
from string_calculator import calculator
import pytest
import logging
import random


logger = logging.getLogger(__file__)


def generate_data_with_two_delimiter(n: int) -> tuple[str, int]:
    data = ""
    sum_val = 0
    while n > 0:
        dl = random.choice(["\n", ","])
        number = random.randint(1, 10000)
        data += str(number) + dl
        # update data generator
        if number > 1000:
            continue
        sum_val += number
        n -= 1
    return data, sum_val


generate_with_10_integers = generate_data_with_two_delimiter(10)
generate_with_20_integers = generate_data_with_two_delimiter(20)
generate_with_100_integers = generate_data_with_two_delimiter(100)


def generate_data_with_custom_delimiter(n: int, delimiter: str) -> tuple[str, int]:
    data = ""
    sum_val = 0
    prefix = f"//{delimiter}\n"
    while n > 0:
        number = random.randint(1, 10000)
        data += str(number) + delimiter
        # update data generator
        if number > 1000:
            continue
        sum_val += number
        n -= 1
    data = prefix + data
    return data, sum_val


class TestCalculator:
    def test_module_has_add_method(self):
        """
        test to check if calculator has add function or not
        """
        logger.info("Running test case for method check in module")
        assert hasattr(calculator, "add")

    def test_add_signature(self):
        """
        add method should accept
        1. Only one parameter numbers of type string
        2. It returns data of type integer
        """
        logger.info("Running test case for add method signature")
        args_details = inspect.getfullargspec(calculator.add)
        assert len(args_details.args) == 1
        assert "numbers" in args_details.args
        assert issubclass(args_details.annotations["numbers"], str)
        assert issubclass(args_details.annotations["return"], int)

    @pytest.mark.parametrize(
        "_desc,param,output", [("empty-string-without-spaces", "", 0), ("empty-string-with-spaces", " ", 0)]
    )
    def test_add_for_empty_string(self, _desc: str, param: str, output: int):
        """
        add method should accept empty string ""
        1. If empty string should return as 0
        """
        logger.info(f"Running test case for {_desc}")
        result = calculator.add(param)
        assert isinstance(result, int)
        assert result == output

    @pytest.mark.parametrize(
        "_desc,param,output",
        [
            ("check-for-single-integer-as-comma-separated-value", "1", 1),
            ("check-for-two-integer-as-comma-separated-value", "1,5", 6),
            ("check-for-multiple-integer-as-comma-separated-value-1", "1,2,3,4", 10),
            ("check-for-multiple-integer-as-comma-separated-value-2", "100,200,3,4", 307),
            ("check-for-multiple-integer-with-empty-as-comma-separated-value", "1,200,3,,4", 208),
        ],
    )
    def test_add_for_comma_separated_string(self, _desc: str, param: str, output: int):
        """
        add method should accept empty string should accept comma separated value
        """
        logger.info(f"Running test case for {_desc}")
        result = calculator.add(param)
        assert isinstance(result, int)
        assert result == output

    @pytest.mark.parametrize(
        "_desc,param,output",
        [
            ("addition-accept-\\n-delimiter", "\n,", 0),
            ("addition-accept-\\n-delimiter", "1\n2", 3),
            ("addition-accept-\\n-and-,-both-delimiter", "1\n2,3", 6),
            ("addition-accept-\\n-and-,-both-delimiter-with-multiple-inputs", "1\n2,3", 6),
            (
                "addition-accept-\\n-and-,-both-delimiter-with-10-integer",
                generate_with_10_integers[0],
                generate_with_10_integers[1],
            ),
            (
                "addition-accept-\\n-and-,-both-delimiter-with-20-integer",
                generate_with_20_integers[0],
                generate_with_20_integers[1],
            ),
            (
                "addition-accept-\\n-and-,-both-delimiter-with-100-integer",
                generate_with_100_integers[0],
                generate_with_100_integers[1],
            ),
        ],
    )
    def test_addition_can_accept_two_delimiters(self, _desc: str, param: str, output: int):
        """
        add should accept
        `\n` and `,` values to perform addition
        on string of numbers
        """
        logger.info(f"Running test case for {_desc}")
        result = calculator.add(param)
        assert isinstance(result, int)
        assert result == output

    @pytest.mark.parametrize(
        "_desc,n,delimiter",
        [
            ("addition-custom-delimiter-;-1-integer", 1, ";"),
            ("addition-custom-delimiter-*-2-integer", 2, "*"),
            ("addition-custom-delimiter-|-10-integer", 10, "|"),
            ("addition-custom-delimiter-$-20-integer", 20, "$"),
            ("addition-as-without-delimiter-20-integer", 20, ""),
        ],
    )
    def test_addition_can_accept_custom_delimiter(self, _desc: str, n: int, delimiter: str):
        """
        add should accept
        custom any delimiter to perform addition
        on string of numbers
        """
        logger.info(f"Running test case for {_desc}")
        data, sum_val = "", 0
        if delimiter != "":
            data, sum_val = generate_data_with_custom_delimiter(n, delimiter)
        else:
            data, sum_val = generate_data_with_two_delimiter(n)

        result = calculator.add(data)
        assert isinstance(result, int)
        assert result == sum_val

    @pytest.mark.parametrize(
        "_desc,param,error_msg",
        [
            ("addition-throw-error-on-negative-integer-1", "1,-2,3", "negatives not allowed: numbers(-2)"),
            ("addition-throw-error-on-multiple-negative-number-1", "1,-2,-3", "negatives not allowed: numbers(-2,-3)"),
            (
                "addition-throw-error-on-multiple-negative-number-with-new-line-delimiter",
                "1\n-2,-3",
                "negatives not allowed: numbers(-2,-3)",
            ),
            (
                "addition-throw-error-on-multiple-negative-number-with-custom-delimiter",
                "//;\n1;-2;-3",
                "negatives not allowed: numbers(-2,-3)",
            ),
        ],
    )
    def test_addition_through_error_with_negative_number(self, _desc: str, param: str, error_msg: str):
        """
        add should not accept
        negative number should throw error
        """
        logger.info(f"Running test case for {_desc}")
        with pytest.raises(calculator.NegativeNumberError) as exp:
            result = calculator.add(param)
            assert result is None
        assert str(exp.value) == error_msg

    @pytest.mark.parametrize(
        "_desc,param,output",
        [
            ("addition-gt1000-sum-all-lt1000", "1000,1001,3", 1003),
            ("addition-all-number-gt1000-should-0", "1001,1001,1001", 0),
            ("addition-gt1000-sum-all-value-10-integer", "1,2,3,4000,2000,5,10000,8000,79999,1233243", 11),
            (
                "addition-throw-error-on-multiple-negative-number-with-custom-delimiter",
                "//;\n1;2;3;9080;1",
                7,
            ),
        ],
    )
    def test_addition_gt1000(self, _desc: str, param: str, output: int):
        """
        addition of number greater than 1000 should not be included in sum
        """
        logger.info(f"Running test case for {_desc}")
        result = calculator.add(param)
        assert result == output

    @pytest.mark.parametrize(
        "_desc,n,delimiter",
        [
            ("addition-custom-delimiter-;-1-integer", 1, "[;;]"),
            ("addition-custom-delimiter-*-2-integer", 2, "[**]"),
            ("addition-custom-delimiter-|-10-integer", 10, "[||]"),
            ("addition-custom-delimiter-$-20-integer", 20, "[$$$]"),
            ("addition-as-without-delimiter-20-integer", 20, ""),
        ],
    )
    def test_addition_can_accept_custom_delimiter_with_multiple_length(self, _desc: str, n: int, delimiter: str):
        """
        add should accept
        custom any delimiter to perform addition
        on string of numbers
        """
        logger.info(f"Running test case for {_desc}")
        data, sum_val = "", 0
        if delimiter != "":
            data, sum_val = generate_data_with_custom_delimiter(n, delimiter)
        else:
            data, sum_val = generate_data_with_two_delimiter(n)

        result = calculator.add(data)
        assert isinstance(result, int)
        assert result == sum_val

    @pytest.mark.parametrize(
        "_desc,n,delimiter",
        [
            ("addition-custom-delimiter-[;][*]-1-integer", 1, "[;][*]"),
            ("addition-custom-delimiter-[;][*][U]-1-integer", 0, "[;][*][U]"),
            ("addition-custom-delimiter-[*][;]-2-integer", 2, "[*][;]"),
            ("addition-custom-delimiter-[|][#]-10-integer", 10, "[|][#]"),
            ("addition-custom-delimiter-[$][;][PP][^^][&&]-20-integer", 20, "[$][;][PP][^^][&&]"),
            ("addition-as-without-delimiter-20-integer", 20, ""),
        ],
    )
    def test_addition_can_accept_multiple_custom_delimiter_with_single_length(self, _desc: str, n: int, delimiter: str):
        """
        add should accept
        multiple delimiter with single characters
        ex: [*], [*][;], [|][#]
        on string of numbers
        """
        logger.info(f"Running test case for {_desc}")
        data, sum_val = "", 0
        if delimiter != "":
            data, sum_val = generate_data_with_custom_delimiter(n, delimiter)
        else:
            data, sum_val = generate_data_with_two_delimiter(n)

        result = calculator.add(data)
        assert isinstance(result, int)
        assert result == sum_val

    @pytest.mark.parametrize(
        "_desc,n,delimiter",
        [
            ("addition-custom-delimiter-[;;][**][()()]-1-integer", 1, "[;;][**][()()]"),
            ("addition-custom-delimiter-[__][***][UUUU]-1-integer", 0, "[__][***][UUUU]"),
            ("addition-custom-delimiter-[__][***][^^][FF]-2-integer", 2, "[__][***][^^][FF]"),
            ("addition-custom-delimiter-[!!][|][#][&&]-10-integer", 1000, "[!!][|][#][&&]"),
            ("addition-custom-delimiter-[@@][$][;][PP][^^][&&]-20-integer", 100, "[@@][$][;][PP][^^][&&]"),
            ("addition-as-without-delimiter-20-integer", 20, ""),
        ],
    )
    def test_addition_with_multi_custom_delimiter_of_multi_length(self, _desc: str, n: int, delimiter: str):
        """
        add should accept
        multiple delimiter with single characters
        ex: //[;;][**]\n
        on string of numbers
        """
        logger.info(f"Running test case for {_desc}")
        data, sum_val = "", 0
        if delimiter != "":
            data, sum_val = generate_data_with_custom_delimiter(n, delimiter)
        else:
            data, sum_val = generate_data_with_two_delimiter(n)

        result = calculator.add(data)
        assert isinstance(result, int)
        assert result == sum_val