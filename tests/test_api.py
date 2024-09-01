from fastapi import FastAPI
from fastapi.testclient import TestClient
import logging
from api import main

logger = logging.getLogger(__file__)


class TestCalculatorApi:

    def test_setup_api(self):
        logger.info("Running test case for method check in module")
        assert hasattr(main, "api")
        assert isinstance(main.api, FastAPI)
