import pytest
from click.testing import CliRunner
from cli import app
import logging

logger = logging.getLogger(__file__)


def build_text_format(numbers, sum_val):
    return [
        "Output:",
        "==================",
        f"Input: {numbers}",
        f"Addition of numbers: {sum_val}",
        "==================",
    ]


class TestCliApp:
    def test_has_main_method(self):
        """
        test to check if calculator has add function or not
        """
        logger.info("Running test case for method check in module")
        assert hasattr(app, "main")

    def test_cli_app_accepts_number_parameters(self):
        runner = CliRunner()
        with runner.isolation():
            result = runner.invoke(app.main, ["--numbers", ""])
            assert result.exit_code == 0
            assert result.output.strip() == "\n".join(build_text_format("", 0))

    def test_cli_app_accepts_number_parameters_with_delimited_numbers(self):
        runner = CliRunner()
        with runner.isolation():
            result = runner.invoke(app.main, ["--numbers", "1,2"])
            assert result.exit_code == 0
            assert result.output.strip() == "\n".join(build_text_format("1,2", 3))

    @pytest.mark.parametrize("_desc,param,output", [
        ("addition-numbers-with-comma-formatted", "1,2,3,4", 10),
        ("addition-numbers-with-\n-comma-formatted", "1\n2,3,4", 10),
        ("addition-numbers-with-//$\n-formatted", "//$\n1$2$3$4", 10)
        ])
    def test_cli_app_perform_addition_with_multiple_numbers(self, _desc: str, param: str, output: int):
        runner = CliRunner()
        logger.info(f"Executing test for {_desc}")
        with runner.isolation():
            result = runner.invoke(app.main, ["--numbers", param])
            assert result.exit_code == 0
            assert result.output.strip() == "\n".join(build_text_format(param, output))
