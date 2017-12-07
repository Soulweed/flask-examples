# Install the Python Requests library:
# `pip install requests`

import requests
import json

def send_request():
    # Request weather underground
    # GET http://api.wunderground.com/api/380538e19b591277/conditions/q/TH/Bangkok.json

    try:
        response = requests.get(
            url="http://api.wunderground.com/api/380538e19b591277/conditions/q/TH/Bangkok.json",
        )
        if response.status_code == 200:
            print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
            print('Response HTTP Response Body: {content}'.format(
            content=response.content))
            return response.content
        else:
            print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
            return None

    except requests.exceptions.RequestException:
        print('HTTP Request failed')
        return None


def main():
    print("Start Program")
    result = send_request()
    output = json.loads(result)
    print(type(result))
    print(type(output))

if __name__ == '__main__':
    main()

