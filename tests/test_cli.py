from click.testing import CliRunner
from cli import app
import logging

logger = logging.getLogger(__file__)


class TestCliApp:
   
    def test_has_main_method(self):
        """
        test to check if calculator has add function or not
        """
        logger.info("Running test case for method check in module")
        assert hasattr(app, "main")