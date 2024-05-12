import ConversorFuncoes

choices = [None, None, None, None]
unit = None
distance_valous = [1000, 1, 0.01, 0.0001]
distance_symbols = ["km", "m", "cm", "mm"]
area_valous = [1000000, 1, 0.0001, 0.000001]
area_symbols = ["km²", "m²", "cm²", "mm²"]
volume_valous = [1000, 1, 0.001, 0.001]
volume_symbols = ["m³", "l", "ml", "cm³"]
info_valous = [1, 8, 8192, 8388608, 8589934592, 8796093022208, 9007199254740992, 9223372036854775808, 9444732965739290427392, 9671406556917033397649408]
info_symbols = ["bit", "Byte", "KB", "MB", "GB", "TB", "PB", "EB", "ZB", "YB"]
massa_valous = [1000, 1, 0.001, 0.000001]
massa_symbols = ["t", "kg", "g", "mg"]

while True:
    choices[0] = ConversorFuncoes.Menu1()

#Sair:
    if choices[0] == 0:
        print("Finalizando Sistema...")
        print("Sistema Finalizado.")
        break

#Distancia:
    elif choices[0] == 1:
        while True:
            choices[1] = ConversorFuncoes.Menu2()
            if choices[1] == 0:
                break
            else:
                try:
                    unit = int(input("Sistema: Qual O Valor Dessa Unidade?: "))
                    ConversorFuncoes.Limpar_Terminal()
                except:
                    print("Sistema: 3RR0R! \n")
            choices[2] = ConversorFuncoes.Menu3()
            if choices[2] == 0:
                pass
            else:
                print(f"{unit}{distance_symbols[choices[1] - 1]} = {unit * (distance_valous[choices[1] - 1] / distance_valous[choices[2] - 1])}{distance_symbols[choices[2] - 1]}")
                print()
                while True:
                    choices[3] = input("Sistema: Deseja Converter Outro Valor?: ").lower()
                    if choices[3] == "s" or choices[3] == "sim" or choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                        break
                    else:
                        print("Sistema: 3RR0R!")
                        print()
                if choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                    break
                else:
                    pass

#Area:
    elif choices[0] == 2:
        while True:
            choices[1] = ConversorFuncoes.Menu2()
            if choices[1] == 0:
                break
            else:
                try:
                    unit = int(input("Sistema: Qual O Valor Dessa Unidade?: "))
                    ConversorFuncoes.Limpar_Terminal()
                except:
                    print("Sistema: 3RR0R! \n")
            choices[2] = ConversorFuncoes.Menu3()
            if choices[2] == 0:
                pass
            else:
                print(f"{unit}{area_symbols[choices[1] - 1]} = {unit * (area_valous[choices[1] - 1] / area_valous[choices[2] - 1])}{area_symbols[choices[2] - 1]}")
                print()
                while True:
                    choices[3] = input("Sistema: Deseja Converter Outro Valor?: ").lower()
                    if choices[3] == "s" or choices[3] == "sim" or choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                        break
                    else:
                        print("Sistema: 3RR0R!")
                        print()
                if choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                    break
                else:
                    pass

#Volume:
    elif choices[0] == 3:
        while True:
            choices[1] = ConversorFuncoes.Menu4()
            if choices[1] == 0:
                break
            else:
                try:
                    unit = int(input("Sistema: Qual O Valor Dessa Unidade?: "))
                    ConversorFuncoes.Limpar_Terminal()
                except:
                    print("Sistema: 3RR0R! \n")
            choices[2] = ConversorFuncoes.Menu5()
            if choices[2] == 0:
                pass
            else:
                print(f"{unit}{volume_symbols[choices[1] - 1]} = {unit * (volume_valous[choices[1] - 1] / volume_valous[choices[2] - 1])}{volume_symbols[choices[2] - 1]}")
                print()
                while True:
                    choices[3] = input("Sistema: Deseja Converter Outro Valor?: ").lower()
                    if choices[3] == "s" or choices[3] == "sim" or choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                        break
                    else:
                        print("Sistema: 3RR0R!")
                        print()
                if choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                    break
                else:
                    pass

#Informação:
    elif choices[0] == 4:
        while True:
            choices[1] = ConversorFuncoes.Menu6()
            if choices[1] == 0:
                break
            else:
                try:
                    unit = int(input("Sistema: Qual O Valor Dessa Unidade?: "))
                    ConversorFuncoes.Limpar_Terminal()
                except:
                    print("Sistema: 3RR0R! \n")
            choices[2] = ConversorFuncoes.Menu7()
            if choices[2] == 0:
                pass
            else:
                print(f"{unit}{info_symbols[choices[1] - 1]} = {unit * (info_valous[choices[1] - 1] / info_valous[choices[2] - 1])}{info_symbols[choices[2] - 1]}")
                print()
                while True:
                    choices[3] = input("Sistema: Deseja Converter Outro Valor?: ").lower()
                    if choices[3] == "s" or choices[3] == "sim" or choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                        break
                    else:
                        print("Sistema: 3RR0R!")
                        print()
                if choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                    break
                else:
                    pass

#Massa:
    elif choices[0] == 5:
        while True:
            choices[1] = ConversorFuncoes.Menu8()
            if choices[1] == 0:
                break
            else:
                try:
                    unit = int(input("Sistema: Qual O Valor Dessa Unidade?: "))
                    ConversorFuncoes.Limpar_Terminal()
                except:
                    print("Sistema: 3RR0R! \n")
            choices[2] = ConversorFuncoes.Menu9()
            if choices[2] == 0:
                pass
            else:
                print(f"{unit}{massa_symbols[choices[1] - 1]} = {unit * (massa_valous[choices[1] - 1] / massa_valous[choices[2] - 1])}{massa_symbols[choices[2] - 1]}")
                print()
                while True:
                    choices[3] = input("Sistema: Deseja Converter Outro Valor?: ").lower()
                    if choices[3] == "s" or choices[3] == "sim" or choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                        break
                    else:
                        print("Sistema: 3RR0R!")
                        print()
                if choices[3] == "n" or choices[3] == "nao" or choices[3] == "não":
                    break
                else:
                    pass
