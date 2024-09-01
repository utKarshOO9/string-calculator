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

    def test_calculator_api_post(self):
        logger.info("Running test case for calculator api with post method")
        """
            Api should have calculator api
                METHOD: POST
                ACCEPT PAYLOAD:
                    {
                        "numbers": ""
                    }
                RETURN RESPONSE
                    {
                        "input": "",
                        "output": 0,
                        "errors": []
                    }
        """
        client = TestClient(main.api)
        payload = {"numbers": ""}
        expected = {
                        "input": "",
                        "output": 0,
                        "errors": []
                    }
        response = client.post("/calculator", json=payload)
        assert response.status_code == 200
        assert response.json() == expected

