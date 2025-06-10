import os

os.system("cls")

animais = []


# Menu das metas

def local_metas(usuario):
    caminho = f"{os.path.dirname(__file__)}\clientes\{usuario}"
    return caminho

def adicionar_metas(arquivo):
    os.system("cls")
    novaMeta = input("Nova meta: ")
    file = open(f"{arquivo}\metas.txt", "a")
    file.write(f"{novaMeta}|Pendente\n")
    file.close()
    os.system("cls")
    print("***************************")
    print("")
    print("Meta adicionada com sucesso.")
    print("")
    print("***************************")

def listagem_metas(arquivo):
    file = open(f"{arquivo}\metas.txt", "r")
    conteudo = file.readlines()
    file.close()
    print(f"\nLista de metas e situação:")
    for i in range(len(conteudo)):
        status = conteudo[i].split("|")
        print(f"{i + 1} - {status[0]} | {status[1]}", end="")
    print()

def atualizar_metas(arquivo):
    file = open(f"{arquivo}\metas.txt", "r")
    conteudo = file.readlines()
    file.close()
    os.system("cls")
    print(f"Selecione uma meta para atualizar:")
    for i in range(len(conteudo)):
        status = conteudo[i].split("|")
        print(f"{i + 1} - {status[0]} | {status[1]}", end="")
    escolha_meta = int(input("Escolha: ")) - 1
    os.system("cls")
    print("Selecione a informação que deseja atualizar:")
    print("1 - Nome da meta\n2 - Situação da meta")
    escolha_meta_info = int(input("Escolha: ")) - 1

    status = conteudo[escolha_meta].split("|")
    if escolha_meta_info == 0:
        status[escolha_meta_info] = str(input("Insira o novo nome da meta: "))
    elif escolha_meta_info == 1:
        if status[escolha_meta_info] == "Pendente\n":
            status[escolha_meta_info] = "Concluída\n"
        elif status[escolha_meta_info] == "Concluída\n":
            status[escolha_meta_info] = "Pendente\n"
    
    conteudo[escolha_meta] = f"{status[0]}|{status[1]}"

    file = open(f"{arquivo}\metas.txt", "w")
    for value in conteudo:
        file.write(value)
    file.close()
    print("Meta atualizada com sucesso.")

def deletar_metas(arquivo):
    file = open(f"{arquivo}\metas.txt", "r")
    conteudo = file.readlines()
    file.close()
    os.system("cls")
    print(f"Selecione uma meta para deletar:")
    for i in range(len(conteudo)):
        status = conteudo[i].split("|")
        print(f"{i + 1} - {status[0]} | {status[1]}", end="")
    escolha_meta = int(input("Escolha: ")) - 1
    conteudo.pop(escolha_meta)
    file = open(f"{arquivo}\metas.txt", "w")
    for value in conteudo:
        file.write(value)
    file.close()
    print("Meta deletada com sucesso.")

def menu_metas(usuario):
    os.system("cls")
    while True:
        print ("")
        print("***************************")
        print(" - Menu de Metas - ")
        print("1 - Adicionar ")
        print("2 - Listar metas")
        print("3 - Atualizar")
        print("4 - Deletar")
        print("0 - Voltar")
        print("***************************")
        input0 = int(input("opcao: "))

        if input0 == 0:
            break
        elif input0 == 1:
            adicionar_metas(local_metas(usuario))
        elif input0 == 2:
            os.system("cls")
            listagem_metas(local_metas(usuario))
        elif input0 == 3:
            atualizar_metas(local_metas(usuario))
        elif input0 == 4:
            deletar_metas(local_metas(usuario))


# Menu dos pets
def local(usuario):
    # Local da pasta onde estão os arquivos dos pets
    file0 = open(f"{os.path.dirname(__file__)}\clientes\{usuario}\pasta_pets.txt", "r")
    local_pasta_pets = file0.readline()
    file0.close()
    return f"{os.path.dirname(__file__)}\clientes\{usuario}\{local_pasta_pets}"

def adicionar_pets(local_pasta_pets):
    os.system("cls")

    animal = str(input("Digite o nome do seu pet: "))
    animais.append(animal)

    arquivo = animal + ".txt"
    file = open(f"{local_pasta_pets}\{arquivo}", "x")
    especie = str(input("Digite a especie do seu pet: "))
    raca= str(input("Digite a raça do seu pet: "))
    nasc = str(input("Digite o nascimento do seu pet: "))
    peso = str(input("Digite o peso do seu pet: "))
    file.write(f"{animal}\n{especie}\n{raca}\n{nasc}\n{peso}")
    file.close()
    
    os.system("cls")
    print("Pet adicionado com sucesso.\n")

def listagem_pets(local_pasta_pets):
    os.system("cls")

    print("Lista de Pets:")
    for i in range(len(animais)):
        arquivo = animais[i] + ".txt"
        fileR = open(f"{local_pasta_pets}\{arquivo}", "r")
        conteudo = fileR.readlines()
        fileR.close()

        print(f"{i+1}º Pet\nNome: {conteudo[0]}Espécie: {conteudo[1]}Raça: {conteudo[2]}Nascimento: {conteudo[3]}Peso: {conteudo[4]}\n")

def atualizar_pets(local_pasta_pets):
    os.system("cls")
        
    print(f"Selecione o pet que você deseja atualizar:")
    for i in range(len(animais)):
        print(f"{i + 1} - {animais[i]}")
    escolha_pet = int(input("Escolha: ")) - 1

    arquivo = animais[escolha_pet] + ".txt"
    lendo = open(f"{local_pasta_pets}\{arquivo}", "r")
    conteudo = lendo.readlines()
    lendo.close()

    print("Qual informação você quer atualizar?\n1 - Nome\n2 - Espécie\n3 - Raça\n4 - Nascimento\n5 - Peso")
    escolha_info = int(input("Escolha: ")) - 1
    nova_info = str(input("Digite a nova informação: "))
    conteudo[escolha_info] = nova_info + "\n"
    atualizando = open(f"{local_pasta_pets}\{arquivo}", "w")
    
    for value in conteudo:
        atualizando.write(value)
    atualizando.close()

    if escolha_info == 0:
        animais[escolha_pet] = nova_info
        os.rename(f"{local_pasta_pets}\{arquivo}", f"{local_pasta_pets}\{nova_info}.txt")
    
    os.system("cls")
    print("Atulização realizada com sucesso.\n")

def deletar_pets(local_pasta_pets):
    os.system("cls")

    print("Selecione o pet que deseja deletar:")
    for i in range(len(animais)):
        print(f"{i + 1} - {animais[i]}")
    escolha_pet = int(input("Escolha: ")) - 1
    
    if animais[escolha_pet] in animais:
        arquivo = animais[escolha_pet] + ".txt"
        animais.pop(escolha_pet)
        os.remove(f"{local_pasta_pets}\{arquivo}")

        os.system("cls")
        print("Realizado com sucesso.\n")
    else:
        os.system("cls")
        print("Esse pet não foi registrado.\n")

def armazenamento_pets(usuario):
    os.system("cls")

    print("Selecione o local de armazenamento dos dados dos pets.\n1 - Criar uma pasta (Não haverá qualquer informação inicial)\n2 - Indicar uma pasta (Caso tenha alguma informação de pet salvo\nda maneira correta na pasta indicada, será adicionado automaticamente)")
    escolha_local = int(input("Escolha: "))

    # criar pasta 
    if escolha_local == 1:
        os.system("cls")
        while True:
            local_pasta_pets = str(input("Digite o nome da pasta que deseja criar: "))
            pasta_pets = open(f"{os.path.dirname(__file__)}\clientes\{usuario}\pasta_pets.txt", "w")
            pasta_pets.write(local_pasta_pets)
            pasta_pets.close()
            # Local da pasta onde estão os arquivos dos pets
            file0 = open(f"{os.path.dirname(__file__)}\clientes\{usuario}\pasta_pets.txt", "r")
            local_pasta_pets = file0.readline()
            file0.close()
            try:
                os.system(f"mkdir {os.path.dirname(__file__)}\clientes\{usuario}\{local_pasta_pets}")
                print("Pasta criada com sucesso.")
                return 1
            except FileExistsError:
                print(f"Já existe uma pasta com o nome '{local_pasta_pets}'.")
            except Exception as e:
                print(f"Erro inesperado: {e}")
            # Arquivo que já existe
    elif escolha_local == 2:
        os.system("cls")
        local_pasta_pets = str(input("Insira o nome da pasta que deseja utilizar: "))
        pasta_pets = open(f"{os.path.dirname(__file__)}\clientes\{usuario}\pasta_pets.txt", "w")
        pasta_pets.write(local_pasta_pets)
        pasta_pets.close()
        try:
            arquivos = os.listdir(f"{os.path.dirname(__file__)}\clientes\{usuario}\{local_pasta_pets}")
            
            if len(arquivos) > 0:
                for i in range(len(arquivos)):
                    info = arquivos[i].split(".txt")
                    animais.append(info[0])
            print("Pasta encontrada com sucesso.")
            return 1
        
        except FileExistsError:
            print(f"Já existe uma pasta com o nome '{local_pasta_pets}'.")
            return 0
        except Exception as e:
            print(f"Erro inesperado: {e}")
            return 0
        
def menu_pets(usuario):
    while True:
        print("***************************")
        print("- Menu dos pets -")
        print("1 - Adicionar\n2 - Listar pets\n3 - Atualizar\n4 - Deletar\n0 - Voltar")
        print("***************************")
        input0 = int(input("Escolha: "))
    
        if input0 == 0:
            break

        elif input0 == 1:
            try:
                adicionar_pets(local(usuario))
            except FileExistsError:
                print(f"Já existe um animal com esse nome.\n")

        elif input0 == 2:
            listagem_pets(local(usuario))
        
        elif input0 == 3:
            try:
                atualizar_pets(local(usuario))
            except IndexError:
                print(f"Você selecionou um alternativa inválida.")

        elif input0 == 4:
            deletar_pets(local(usuario))


# Menu de Eventos e Cuidados
eventos = {"vacinações": [],"consultas": [],"remédios": []}

def remover_cadastro():
    print("Selecione o número do evento que deseja remover: ")
    arquivo=open("Cadastro_eventos.txt", "r")

    informacao=arquivo.readlines()
    for i in range(len(informacao)):
        print(f"{i+1} . {informacao[i]}")

    linha_excluida=int(input("Digite o evento que você deseja excluir: "))

    arquivo.close()
    arquivo2=open("Cadastro_eventos.txt","w")
    informacao.pop(linha_excluida-1)

    for i in range(len(informacao)):
        arquivo2.write(informacao[i])
    arquivo2.close()
    print("Evento removido com sucesso.")

def cadastrar_evento():
    print("----------------------------------------------------")
    print("\nTipos de evento: vacinações | consultas | remédios")
    print(" ")
    tipo_cadastro = input("Digite o tipo de evento: ").lower()
  
    if tipo_cadastro not in eventos:
        print("Tipo de evento inválido.")
        return
          
    data_cadastro = input("Digite a data do evento : ")
    print(" ")
    nome_pet = input("Digite o nome do pet: ")
    print(" ")
    responsavel = input("Digite o nome do responsável: ")
        
    evento = {
        "data": data_cadastro,
        "pet": nome_pet,
        "responsável": responsavel
    }
         
    eventos[tipo_cadastro].append(evento)
    print(f"\n{tipo_cadastro.capitalize()} cadastrada com sucesso!")
    with open("Cadastro_eventos.txt", "a")as arquivo:
        arquivo.write(f"Tipo: {tipo_cadastro}|pet: {nome_pet}|data: {data_cadastro}|responsável: {responsavel}\n")

def exibir_eventos():
    print("=== Eventos Cadastrados ===")
    arquivo=open("Cadastro_eventos.txt", "r")

    informacao=arquivo.readlines()
    for i in range(len(informacao)):
        print(f"{i+1}º {informacao[i]}")
    arquivo.close()

def menu_cadastro():
    while True:
        print ("****************************")
        print("\n=== Cadastro de eventos ===")
        print("1 - Cadastrar evento")
        print("2 - Exibir eventos")
        print("3 - Editar um evento")
        print("0 - Voltar para o menu principal")
        print ("****************************")
        opcao_cadastro = input("Escolha uma opção: ")

        if opcao_cadastro == "1":
            os.system("cls")
            cadastrar_evento()

        elif opcao_cadastro == "2":
            os.system("cls")
            exibir_eventos()
        elif opcao_cadastro == "0":
            os.system("cls")
            print("Voltando para o menu principal.")
            break
        elif opcao_cadastro == "3":
            os.system("cls")
            remover_cadastro()
        else: 
            print("Opção inválida. Escolha uma das três opções")
            os.system("cls")


def sugestao_cuidados():
    while True: 
        
        especie = input("==== Sugestões ====\n1 - Cachorro\n2 - Gato\n0 - Sair\nopcao:")
        
        if especie == "0":
            os.system("cls")
            print("***************************")
            print("Voltando pro menu principal")
            print("***************************")
            break

        if especie.lower() == "1":
            os.system("cls")
            idade = int(input("Digite a idade do pet em anos: "))
            if idade < 1:
                os.system("cls")
                print("******************************************************************************************")
                print("Sugestão: Brinquedos de borracha macia, ração para filhotes, passeios curtos e frequentes.")
                print("******************************************************************************************")
            elif idade < 7:
                os.system("cls")
                print("*************************************************************************")
                print("Sugestão: Brinquedos interativos, ração para adultos, caminhadas diárias.")
                print("*************************************************************************")
            else:
                os.system("cls")
                print("**********************************************************************************")
                print("Sugestão: Brinquedos leves, ração sênior, exercícios leves como caminhadas curtas.")
                print("**********************************************************************************")
            
        elif especie == "2":
            os.system("cls")
            idade = int(input("Digite a idade do pet em anos: "))
            if idade < 1:
                os.system("cls")
                print("***************************************************************************")
                print("Sugestão: Arranhadores pequenos, ração para filhotes, brinquedos com penas.")
                print("***************************************************************************")
            elif idade < 7:
                os.system("cls")
                print("**********************************************************************************")
                print("Sugestão: Ração para adultos, brinquedos com catnip, sessões de brincadeira ativa.")
                print("**********************************************************************************")
            else:
                os.system("cls")
                print("*****************************************************************************")
                print("Sugestão: Ração sênior, brinquedos leves, ambientes tranquilos para descanso.")
                print("*****************************************************************************")
            
        else:
            os.system("cls")
            print("Digite um número de 1 a 3.\nTente novamente")
            continue


clientes = []
#criação de pasta/diretório de cada cliente
def cadastro():
    os.system("cls")
    print ("Forneça as informações do usuário!")
    print ("**********************************")

    login = input("Login: ")
    senha = input("Senha: ")
    os.system(f"mkdir {os.path.dirname(__file__)}\clientes\{login}")

    file0 = open(f"{os.path.dirname(__file__)}\clientes\{login}\login.txt", "x")
    file0.write(f"{login}\n{senha}")
    file0.close()

    file1 = open(f"{os.path.dirname(__file__)}\clientes\{login}\pasta_pets.txt", "x")
    file1.close()

    file2 = open(f"{os.path.dirname(__file__)}\clientes\{login}\metas.txt", "x")
    file2.close()

    clientes.append(login)

    os.system("cls")

    print("OK! Cadastro concluído.")

#ler a pasta do login do usuário e verificar se a senha está correta
def fazer_login():
    os.system("cls")

    login = input("Usuário: ")
    if login in clientes:
        senha = input("Senha: ")
        file0 = open(f"{os.path.dirname(__file__)}\clientes\{login}\login.txt", "r")
        info = file0.readlines()
        senha_correta = info[1]
        file0.close()
        if senha == senha_correta:
            os.system("cls")
            print("Login realizado com sucesso!")
            return login
        else:
            os.system("cls")
            print("Senha incorreta.")
            return 0
    else:
        os.system("cls")
        print("Esse usuário não está cadastrado.")
        return 0

def mostrarDados():
    os.system("cls")

    print("Lista de usuários: ")
    for i in range(len(clientes)):
        print(f"{clientes[i]}")

def mostrarCliente():

    while True:
        print("")
        print("Usuário cadastrados: ")
        print("")

        for i in clientes:
            print ("Nome" , i["nomeComp"], "Login:",i["login"])

        print("")

        opcao = input("Deseja conferir novamente? (S/N):").strip().lower()
        if(opcao == "n"):
            menu()
            break

def menu():
    arquivos = os.listdir(f"{os.path.dirname(__file__)}\clientes")
    if len(arquivos) > 0:
        for i in range(len(arquivos)):
            clientes.append(arquivos[i])

    while True:
        print("************************************")
        print("[1] Cadastrar usuário")
        print("[2] Efetuar Login")
        print("[3] Consultar usuários")
        print("[0] Encerrar programa")
        print("************************************")

        
        x = int(input("Escolha entre: [1] [2] [3] [0]\n"))

        while x > 3 or x < 0:
            x = int(input("Erro, tente novamente!\nEscolha uma opção:"))

        if x ==1:
            cadastro()
        elif x == 2:
            tentativa = fazer_login()
            if tentativa != 0:
                return tentativa
        elif x == 3:
            mostrarDados()
        else:
            print("Programa encerrado!")
            return 0

