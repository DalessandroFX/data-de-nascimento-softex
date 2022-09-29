stop = False
while stop == False:
    nome = input("qual o seu nome:")
    print("digite sua data de nascimente:")
    try:
        ano = int(input())
        if ano >= 1922 and ano <=2021:
            stop = True
            print(nome," você tem ou vai completar:", 2022-ano)
        else:
            print("você digitou um numero invalido")
    except:
        print("você ditou um valor invalido")