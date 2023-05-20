def executaautomato(estados, estadoInicial, estadosFinais, alfabeto, alfabetopilha, regras, cadeia):

    pilha = ["λ"]

    estadoAtual = estadoInicial
    posicaoCadeia = 0

    while posicaoCadeia < len(cadeia):
        simboloLido = cadeia[posicaoCadeia]
        simboloTopoPilha = pilha[-1]

        if simboloLido not in alfabeto or simboloTopoPilha not in alfabetopilha:
            return False

        if estadoAtual not in regras or simboloLido not in regras[estadoAtual] or simboloTopoPilha not in regras[estadoAtual][simboloLido]:
            return False

        novoEstado = regras[estadoAtual][simboloLido][simboloTopoPilha][1]
        novoSimboloTopoPilha = regras[estadoAtual][simboloLido][simboloTopoPilha][0] if len(regras[estadoAtual][simboloLido][simboloTopoPilha]) > 1 else "λ"

        if simboloTopoPilha != "λ":
            pilha.pop()
        if novoSimboloTopoPilha != "λ":
            pilha.extend(novoSimboloTopoPilha[::-1])
        estadoAtual = novoEstado

        posicaoCadeia += 1

    if posicaoCadeia == len(cadeia) and len(pilha) == 1 and pilha[0] == "λ" and estadoAtual in estadosFinais:
        return True
    else:
        return False
    
nomeArquivo = 'c:/coloque aqui o caminho completo para o arquivo/entrada.txt'
with open(nomeArquivo, 'r', encoding='utf-8') as arquivo:

    conteudo = [linha.strip() for linha in arquivo.readlines()]

    estados = conteudo[0].split()
    estadoInicial = conteudo[1]
    estadosFinais = conteudo[2].split()
    alfabeto = conteudo[3].split()
    alfabeto_pilha = conteudo[4].split()
    regras = {}
    for linha in conteudo[5:]:
        elementos = linha.split()
        if len(elementos) != 5:
            continue
        
        estadoAtual, substituicao, simboloTopoPilhaoriginal, substituicaoresultante, estado_destino = elementos
        if estadoAtual not in regras:
            regras[estadoAtual] = {}
        if substituicao not in regras[estadoAtual]:
            regras[estadoAtual][substituicao] = {}
        regras[estadoAtual][substituicao][simboloTopoPilhaoriginal] = (substituicaoresultante, estado_destino)

cadeiasTeste = conteudo[-2:]
for cadeia in cadeiasTeste:
    if executaautomato(estados, estadoInicial, estadosFinais, alfabeto, alfabeto_pilha, regras, cadeia):
        print("Aceita a cadeia:", cadeia)
    else:
        print("Rejeita a cadeia:", cadeia)
