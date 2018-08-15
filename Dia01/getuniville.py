import requests
resp = requests.get("http://www.univille.br")
print(resp)
print(resp.text)
