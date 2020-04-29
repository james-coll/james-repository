import requests # on cmd type 'pip install requests'
from pprint import pprint
regions = ['gb', 'it'] # Change to your country
with open('test.jpg', 'rb') as fp: # Change 'test.jpg' to image location
    response = requests.post(
        'https://api.platerecognizer.com/v1/plate-reader/',
        data=dict(regions=regions),  
        files=dict(upload=fp),
        headers={'Authorization': 'Token aeac580b984693f5092af9d1c28efa969142d4a9'})
pprint(response.json()) 