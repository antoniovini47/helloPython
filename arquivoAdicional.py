print("Automato para validar palavras com 'aa' ou 'bb'")
b=0
a=input("Quer repetir o código quantas vezes?")
a=int(a)
while (b<=a):
    b=b+1
    palavra = input("Insira a palavra (cadeia de caracteres): ")
    print("Palavra: ", palavra)
    estadoAtual = 0 #0 é Inicial, 3 é Final
    for i in range(len(palavra)):
        caractereAtual = palavra[i]
        if caractereAtual == "a" or caractereAtual == "b":
            if estadoAtual == 0:
                if caractereAtual == "a":
                    estadoAtual = 1
                elif caractereAtual == "b":
                    estadoAtual = 2
            elif estadoAtual == 1:
                if caractereAtual == "a":
                    estadoAtual = 3
                elif caractereAtual == "b":
                    estadoAtual = 2
            elif estadoAtual == 2:
                if caractereAtual == "a":
                    estadoAtual = 1
                elif caractereAtual == "b":
                    estadoAtual = 3
            elif estadoAtual == 3:
                if caractereAtual == "a" or caractereAtual == "b":
                    estadoAtual = 3
        else:
            print("Caractere inválido detectado!")
            estadoAtual=0
            break
    print("Estado final: ", estadoAtual)
    if estadoAtual == 3:
        print("Palavra válida")
    else:
        print("Palavra inválida")