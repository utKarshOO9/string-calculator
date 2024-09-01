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
        "=================="
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
