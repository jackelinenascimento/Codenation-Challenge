import json
import requests

url = "https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=e4f4565c38c25a5e4b1e06e13463422156208553"

answer = {'answer': open('answer.json', 'rb')}
response = requests.post(url=url, files=answer)
print(response.status_code)
print(response.json())
