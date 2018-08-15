import requests
resp = requests.get(
    "http://museu.univille.br:8080/consultamuseu/rest/mobile/busca/7/10/0/enxaimel")
#print(resp)
dados = resp.json()

for umitem in dados:
    print("oid: ", umitem.get("oid"))
    print("Autor: ", umitem.get("autor"))
    print("Nome: ", umitem.get("nome"))
    print("Comprimento: ", umitem.get("comprimento"))
    print("Descricao: ", umitem.get("descricao"))
    print("Ano: ", umitem.get("anoObra"))
    print("Data da última atualização: ", umitem.get("dataUltAtual"))
