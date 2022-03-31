import re                                                                       #regular expression

endereco = "Rua das flores 72, apartamento 1002, Laranjeiras, RJ, 23440-120"    #CEP = 5 dig. + hífen (opicional) + 3 dig.

padrao = re.compile("[0-9]{5}-?[0-9]{3}")                                       #Encontra a regex passada. Um número de 0 a 9 que se repete por 5 vezes, pode ou não ter "-" e é seguido por 3 números de 0 a 9
busca = padrao.search(endereco)                                                 #match

if busca:
    cep = busca.group()
    print(cep)
