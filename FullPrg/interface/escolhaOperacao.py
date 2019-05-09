from FullPrg.interface.escolhaValores import escolheX, escolheY
from FullPrg.funcoes.operacoes import soma, subtracao, multiply, divide
def escolheOperacao():
    saida = False
    esc = 0
    print(f"-="*30)
    print("-= Operações Matemáticas -=")
    print(f"-=" * 30)
    while saida == False:
        esc = int(input("1 - Soma\n2 - Subtração\n3 - Multiplicação\n4 - Divisão\n Escolha: "))
        if esc == 1:
            x = escolheX()
            y = escolheY()
            print(f"A soma de {x} + {y} = {soma(x, y)}")
        elif esc == 2:
            x = escolheX()
            y = escolheY()
            print(f"A subtração de {x} - {y} = {subtracao(x, y)}")
        elif esc == 3:
            x = escolheX()
            y = escolheY()
            print(f"A multiplicação de {x} * {y} = {multiply(x, y)}")
        elif esc == 4:
            x = escolheX()
            y = escolheY()
            result = divide(x, y)
            if isinstance(result, str):
                print(f"{result}")
            else:
                print(f"A divisão de {x} / {y} = {result}")
        opt = int(input("Deseja realizar outra operação ? <S:1/N:2>"))
        if opt == 1:
            saida = False
        else:
            saida = True

escolheOperacao()
