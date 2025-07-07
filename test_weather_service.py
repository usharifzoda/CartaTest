import unittest
from weather_service import WeatherService


class FakeResponse:
    def __init__(self, json_data):
        self._json = json_data
        self.status_code = 200

    def raise_for_status(self):
        pass

    def json(self):
        return self._json


class FakeSession:
    def __init__(self):
        self.last_params = None

    def get(self, url, params=None, timeout=10):
        self.last_params = (url, params, timeout)
        return FakeResponse({"name": "Test City"})


class WeatherServiceTests(unittest.TestCase):
    def test_get_weather_by_zip_returns_response_json(self):
        session = FakeSession()
        service = WeatherService("test-key", session=session)
        result = service.get_weather_by_zip("12345")
        self.assertEqual(result["name"], "Test City")
        expected_params = {
            "zip": "12345,us",
            "appid": "test-key",
        }
        self.assertEqual(session.last_params[0], WeatherService.BASE_URL)
        self.assertEqual(session.last_params[1], expected_params)
        self.assertEqual(session.last_params[2], 10)


if __name__ == "__main__":
    unittest.main()
