Test-Project:
This is a test project for API Test Coverage based on user input (i.e: City, Zip and Coordinates).
The way this framework is designed, would allow any new API call methods to be created within weather_api_test.py
and make use of parents classes with methods with ease and run all the tests together using nose unit test package.

Configuration:
Before running tests PyCharm should be installed (light-weight Community edition is enough). Also:

Install python3
Install pip: 'sudo easy_install pip3' in Terminal
Install nose: 'sudo pip3 install nose' or 'sudo easy_install nose'
Install requests library: 'sudo pip3 install requests'
Following Test Suite is available: weather_api_test.py

Project Files Definition:
http_requests.py ---> This is the low level http request file that has try and except to make sure to handle any http errors gracefully
base_test.py ---> To set up any inital objects for test executions and global variables for any future tests
weather_api_test.py ---> This is the class that has the 3 requested API Tests and verifications

Running of tests
To run tests suite you need to specify in terminal file name of it in command (running in root framework folder):

nosetests -v -s --nologcapture weather_api_test.py

Test Execution Results Screenshot with all 3 tests 
![image](https://user-images.githubusercontent.com/24594697/117600270-a0806580-b119-11eb-9a5e-f709f1cc8cb7.png)
