import funcoes
import os

os.system("cls")

armazenamento = 0

try:
    user = funcoes.menu()
    if user != 0:
        while True:
            os.system("cls")
            print("*******************************")
            print("- Menu principal -")
            print("1 - Pets\n2 - Metas\n3 - Menu de Eventos e Cuidados\n4 - Sugestões \n0 - Encerrar")
            print("*******************************")
            input0 = int(input("Escolha: "))

            if input0 == 0:
                # funcoes.encerrar_pets()
                print("Encerrado.")
                break

            elif input0 == 1:
                os.system("cls")
                if armazenamento != 1:
                    armazenamento = funcoes.armazenamento_pets(user)
                if armazenamento == 1:
                    os.system("cls")
                    funcoes.menu_pets(user)

            elif input0 == 2:
                os.system("cls")
                funcoes.menu_metas(user)

            elif input0 == 3:
                os.system("cls")
                funcoes.menu_cadastro()

            elif input0 == 4:
                os.system("cls")
                funcoes.sugestao_cuidados()

except KeyboardInterrupt:
    print("Programa encerrado.")
except ValueError:
    print("digite um valor inteiro de 0 a 4! ")
    
