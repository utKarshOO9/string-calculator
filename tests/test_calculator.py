import inspect
from string_calculator import calculator

class TestCalculator:
    
    def test_module_has_add_method(self):
        """
            test to check if calculator has add function or not
        """
        assert hasattr(calculator, 'add')

    def test_add_signature(self):
        """
            add method should accept 
            1. Only one parameter numbers of type string
            2. It returns data of type integer
        """
        args_details = inspect.getfullargspec(calculator.add)
        assert len(args_details.args) == 1
        assert 'numbers' in args_details.args
        assert  issubclass(args_details.annotations['numbers'], str)
        assert  issubclass(args_details.annotations['return'], int)

    def test_add_for_empty_string(self):
        """
            add method should accept empty string ""
            1. If empty string should return as 0
        """
        result = calculator.add("")
        assert isinstance(result, int)
        assert result == 0
    
        