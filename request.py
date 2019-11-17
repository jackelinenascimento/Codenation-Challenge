import json
import requests

url = ''

answer = {'answer': open('answer.json', 'rb')}

submit = requests.post('https://api.codenation.dev/v1/challenge/dev-ps/submit-solution?token=39f5292cbc6779850aff60de8066b92ed244ecd1', files=answer)

print(submit.status_code)
