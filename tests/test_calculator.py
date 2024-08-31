from string_calculator import calculator

class TestCalculator:
    
    def test_module_has_add_method(self):
        """
            test to check if calculator has add function or not
        """
        assert hasattr(calculator, 'add')
