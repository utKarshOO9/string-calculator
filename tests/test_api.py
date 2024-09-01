from fastapi import FastAPI
from fastapi.testclient import TestClient
import logging
import pytest
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

    @pytest.mark.parametrize("_desc,numbers,output", [
        ("api-accept-csv-numbers", "1,2,3", 6),
        ("api-accept-new-line-with-comma", "1\n2,3", 6),
        ("api-accept-multiple-delimiter", "//$\n1$2$3$99090", 6),
    ])
    def test_calculator_api_accept_multiple_number_formats(self, _desc, numbers, output):
        logger.info(f"Running test case {_desc}")
        client = TestClient(main.api)
        payload = {"numbers": numbers}
        expected = {
                        "input": numbers,
                        "output": output,
                        "errors": []
                    }
        response = client.post("/calculator", json=payload)
        assert response.status_code == 200
        assert response.json() == expected

    
    @pytest.mark.parametrize("_desc,numbers,output,error_msg", [
        ("api-should-not-accept-negative-number", "1,-2,3", None, "negatives not allowed: numbers(-2)"),
        ("api-should-not-accept-negative-number-newline", "1,-2\n-3", None, "negatives not allowed: numbers(-2,-3)"),
    ])
    def test_calculator_api_error_validation(self, _desc, numbers, output, error_msg):
        logger.info(f"Running test case {_desc}")
        client = TestClient(main.api)
        payload = {"numbers": numbers}
        expected = {
                        "input": numbers,
                        "output": output,
                        "errors": [error_msg]
                    }
        response = client.post("/calculator", json=payload)
        assert response.status_code == 200
        assert response.json() == expected
