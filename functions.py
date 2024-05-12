def Limpar_Terminal():
    from os import name
    from os import system
    sistema_operacional = name
    if sistema_operacional == 'posix':  # Para sistemas UNIX (Linux, macOS)
        system('clear')
    elif sistema_operacional == 'nt':  # Para Windows
        system('cls')

def Menu1():
    while True:
        try:
            Limpar_Terminal()
            print("|--------------------------------------MENU---------------------------------------|")
            print("|  1 - Distância / 2 - Área / 3 - Volume / 4 - Informação / 5 - Massa / 0 - Sair  |")
            print("|---------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Qual Tipo De Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 5:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu2():
    while True:
        try:
            Limpar_Terminal()
            print("|--------------------------------------MENU----------------------------------------|")
            print("| 1 - Quilometro  /  2 - Metro  /  3 - Centimetro  /  4 - Milimetro  /  0 - Voltar |")
            print("|----------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 4:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu3():
    while True:
        try:
            Limpar_Terminal()
            print("|--------------------------------------MENU----------------------------------------|")
            print("| 1 - Quilometro  /  2 - Metro  /  3 - Centimetro  /  4 - Milimetro  /  0 - Voltar |")
            print("|----------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Para Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 4:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu4():
    while True:
        try:
            Limpar_Terminal()
            print("|--------------------------------------MENU---------------------------------------|")
            print("|   1 - Metro  /  2 - Litro  /  3 - Mililitro  /  4 - Centimetro  /  0 - Voltar   |")
            print("|---------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 4:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu5():
    while True:
        try:
            Limpar_Terminal()
            print("|--------------------------------------MENU---------------------------------------|")
            print("|   1 - Metro  /  2 - Litro  /  3 - Mililitro  /  4 - Centimetro  /  0 - Voltar   |")
            print("|---------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Para Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 4:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu6():
    while True:
        try:
            Limpar_Terminal()
            print("|-------------------------------------------MENU---------------------------------------------|")
            print("|  1 - Bit  /  2 - Byte  /  3 - Kilobyte  /  4 - Megabyte  /  5 - Gigabyte  /  6 - Terabyte  |")
            print("|      7 - Petabyte  /  8 - Exabyte  /  9 - Zettabyte  /  10 - Yottabyte  /  0 - Voltar      |")
            print("|--------------------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 10:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu7():
    while True:
        try:
            Limpar_Terminal()
            print("|-------------------------------------------MENU---------------------------------------------|")
            print("|  1 - Bit  /  2 - Byte  /  3 - Kilobyte  /  4 - Megabyte  /  5 - Gigabyte  /  6 - Terabyte  |")
            print("|      7 - Petabyte  /  8 - Exabyte  /  9 - Zettabyte  /  10 - Yottabyte  /  0 - Voltar      |")
            print("|--------------------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Para Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 10:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu8():
    while True:
        try:
            Limpar_Terminal()
            print("|--------------------------------------MENU---------------------------------------|")
            print("|  1 - Tonelada  /  2 - kilograma  /  3 - Grama  /  4 - Miligrama  /  0 - Voltar  |")
            print("|---------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 4:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor

def Menu9():
    while True:
        try:
            Limpar_Terminal()
            print("|--------------------------------------MENU---------------------------------------|")
            print("|  1 - Tonelada  /  2 - kilograma  /  3 - Grama  /  4 - Miligrama  /  0 - Voltar  |")
            print("|---------------------------------------------------------------------------------| \n")
            valor = int(input("Sistema: Para Qual Unidade De Medida Deseja Converter?: "))
            if 0 <= valor <= 4:
                break
            else:
                print("Sistema: 3RR0R! \n")
        except:
            print("Sistema: 3RR0R! \n")
    Limpar_Terminal()
    return valor
