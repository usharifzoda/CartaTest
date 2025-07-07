import requests


class WeatherService:
    """Service for retrieving weather data from OpenWeatherMap."""

    BASE_URL = "http://api.openweathermap.org/data/2.5/weather"

    def __init__(self, api_key: str, session: requests.Session | None = None):
        self.api_key = api_key
        self.session = session or requests.Session()

    def get_weather_by_zip(self, zip_code: str, country_code: str = "us") -> dict:
        """Return weather information for the given zip code.

        Parameters
        ----------
        zip_code: str
            Zip code to query.
        country_code: str, default "us"
            Optional country code.
        Returns
        -------
        dict
            Parsed JSON from the API.

        Raises
        ------
        RuntimeError
            If the request fails.
        """
        params = {"zip": f"{zip_code},{country_code}", "appid": self.api_key}
        try:
            response = self.session.get(self.BASE_URL, params=params, timeout=10)
            response.raise_for_status()
        except requests.RequestException as exc:
            raise RuntimeError(f"Failed to fetch weather: {exc}") from exc
        return response.json()
