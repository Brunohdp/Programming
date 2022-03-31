idades = [39, 30, 27, 18]
# print(idades)
# idades.append(15)
# print(idades)
#
# for idade in idades:
#     print(idade)
#
# if 15 in idades:
#     idades.remove(15)
#
# # idades.append([55, 33])
# # print(idades)
#
# for elemento in idades:
#     print(f'Recebendo o elemento: {elemento}')
#
# idades.extend([55, 33])
# print(idades)
#
# for cada in idades:
#     print(f'Recebendo o elemento: {cada}')

# idades_no_ano_que_vem = []
# for idade in idades:
#     idades_no_ano_que_vem.append(idade+1)
# print(idades_no_ano_que_vem)
#
# idades_no_ano_que_vem = [(idade+1) for idade in idades]
# print(idades_no_ano_que_vem)
#
# print(maior_de_idade)
# maior_de_idade = [(idade) for idade in idades if idade > 21]

def faz_processamento_de_visualização(lista):
    print(len(lista))

faz_processamento_de_visualização(idades)
