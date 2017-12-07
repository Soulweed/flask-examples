# Install the Python Requests library:
# `pip install requests`

import requests
import json


def send_request():
    # Request
    # POST https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/bc0be351-9374-49b2-8bf5-8a4ec10b0623/url
    print('Function Call')
    try:
        response = requests.post(
            url="https://southcentralus.api.cognitive.microsoft.com/customvision/v1.0/Prediction/bc0be351-9374-49b2-8bf5-8a4ec10b0623/url",
            params={
                "iterationId": "14e84505-8678-4e68-a643-48335244192b",
            },
            headers={
                "Content-Type": "application/json",
                "Prediction-Key": "b0121d7e477d4ec19964813307a723d3",
            },
            data=json.dumps({
                "Url": "https://www.bhphotovideo.com/images/images500x500/tp_link_hs100_wi_fi_smart_plug_1208066.jpg"
            })
        )
        print('Response HTTP Status Code: {status_code}'.format(
            status_code=response.status_code))
        print('Response HTTP Response Body: {content}'.format(
            content=response.content))
    except requests.exceptions.RequestException:
        print('HTTP Request failed')

#
# def main():
#     print("Start Program")
#
#
#
if __name__ == '__main__':
    send_request()