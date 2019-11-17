import json
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=39f5292cbc6779850aff60de8066b92ed244ecd1"

answer = {'answer': open('answer.json', 'rb')}
response = requests.post(url=url, files=answer)
print(response.status_code)
print(response.json())
