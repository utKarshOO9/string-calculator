import inspect
from string_calculator import calculator
import pytest
import logging


logger = logging.getLogger(__file__)


class TestCalculator:
    
    def test_module_has_add_method(self):
        """
            test to check if calculator has add function or not
        """
        logger.info("Running test case for method check in module")
        assert hasattr(calculator, 'add')

    def test_add_signature(self):
        """
            add method should accept 
            1. Only one parameter numbers of type string
            2. It returns data of type integer
        """
        logger.info("Running test case for add method signature")
        args_details = inspect.getfullargspec(calculator.add)
        assert len(args_details.args) == 1
        assert 'numbers' in args_details.args
        assert  issubclass(args_details.annotations['numbers'], str)
        assert  issubclass(args_details.annotations['return'], int)

    @pytest.mark.parametrize("_desc,param,output", [
        ("empty-string-without-spaces", "", 0),
        ("empty-string-with-spaces", " ", 0)
    ])
    def test_add_for_empty_string(self, _desc: str, param: str, output: int):
        """
            add method should accept empty string ""
            1. If empty string should return as 0
        """
        logger.info(f"Running test case for {_desc}")
        result = calculator.add(param)
        assert isinstance(result, int)
        assert result == output

    @pytest.mark.parametrize("_desc,param,output", [
        ("check-for-single-integer-as-comma-separated-value", "1", 1),
        ("check-for-two-integer-as-comma-separated-value", "1,2", 3),
        ("check-for-multiple-integer-as-comma-separated-value-1", "1,2,3,4", 10),
        ("check-for-multiple-integer-as-comma-separated-value-2", "100,200,3,4", 307),
        ("check-for-multiple-integer-with-empty-as-comma-separated-value", "1,200,3,,4", 208),
    ])
    def test_add_for_comma_separated_string(self, _desc: str, param: str, output: int):
        """
            add method should accept empty string should accept comma separated value
        """
        logger.info(f"Running test case for {_desc}")
        result = calculator.add(param)
        assert isinstance(result, int)
        assert result == output

    
        