import requests
from acesso_cep import BuscaEndereco
cep = 18606020

objecto_cep = BuscaEndereco(cep)
bairro, cidade, uf = objecto_cep.acessa_via_cep()

print(f'UF: {uf}\nCidade: {cidade}\nBairro: {bairro}')


# r = requests.get("https://viacep.com.br/ws/01001000/json/")
# print(r.text)
