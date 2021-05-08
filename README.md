Test-Project
This is test project for API Coverage based on user input (i.e: City, Zip and Coordinates)
The way this test is designed would allow any new API call methods to be created within weather_api_test.py
and make use of parents classes with ease and run all the tests together.

Configuration
Before running tests PyCharm should be installed (light-weight Community edition is enough). Also:

Install python3
Install pip: 'sudo easy_install pip3' in Terminal
Install nose: 'sudo pip3 install nose' or 'sudo easy_install nose'
Install requests library: 'sudo pip3 install requests'
Following Test Suite is available: weather_api_test.py

Running of tests
To run tests suite you need to specify in terminal file name of it in command (running in root framework folder):

nosetests -v -s --nologcapture weather_api_test.py
