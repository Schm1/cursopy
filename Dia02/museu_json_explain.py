import requests
resp = requests.get(
    "http://museu.univille.br:8080/consultamuseu/rest/mobile/museus")
#print(resp)
dados = resp.json()

for ummuseu in dados:
    print("oid: ", ummuseu.get("oid"))
    print("Nome: ", ummuseu.get("nome"))
    print("Endereco: ", ummuseu.get("endereco"))
    print("Cidade: ", ummuseu.get("cidade"))
