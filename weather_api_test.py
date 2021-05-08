import requests
from nose.tools import assert_equals
from base_test import BaseTest


class WeatherAPITests(BaseTest):

    def setUp(self):
        super(WeatherAPITests, self).setUp()

    def test_get_weather_by_city(self):
        city_input = input("Enter a city name to get the weather: ")
        print("User city input is: " + city_input)
        url = f"http://api.openweathermap.org/data/2.5/weather?q={city_input}&appid={self.API_KEY}"
        response = self.api_requests.get_request(url).json()

        returned_city = response["name"]
        print("Returned City is: " + returned_city)
        assert_equals(city_input, returned_city, "Input City and Returned City from Json should be equal")

    def test_get_weather_by_zip(self):
        zip_input = input("Enter city zip code to get the weather: ")
        print("User ZIP Code input is: " + zip_input)
        url = f"http://api.openweathermap.org/data/2.5/weather?zip={zip_input},us&appid={self.API_KEY}"
        response = self.api_requests.get_request(url).json()
        city_by_zip = response["name"]
        # print(response)

        if zip_input == "10007":
            assert_equals(city_by_zip, "New York", "ZIP Code 10007 should correspond to New York")
        elif zip_input == "94040":
            assert_equals(city_by_zip, "Mountain View", "ZIP Code 94040 should correspond to New York")
        else:
            print("City corresponding to " + zip_input + " is " + city_by_zip)

    def test_get_weather_by_coordinate(self):
        lat_input = input("Enter city latitude: ")
        lon_input = input("Enter city longitude: ")
        url = f"http://api.openweathermap.org/data/2.5/weather?lat={lat_input}&lon={lon_input}&appid={self.API_KEY}"
        response = self.api_requests.get_request(url).json()
        # print(response)
        coord_by_lat = response["coord"]["lat"]
        coord_by_lon = response["coord"]["lon"]
        response_city = response["name"]
        print("User entered: " + str(coord_by_lat) + " and " + str(coord_by_lon) + " corresponds to: " + response_city)
        assert_equals(lat_input,str(coord_by_lat), "User latitude input and response from API doesn't match")
        assert_equals(lon_input, str(coord_by_lon), "User Longitude input and response from API doesnt match")