from script.process import Processo # Importa a classe Processo do módulo process

processo = Processo() # Cria uma instância da classe Processo
print("--------------------------------")
print("Bem vindo(a) ao OrgaMe!")
creden = input("Por favor, insira seu usuário e senha para iniciar:")
username, password = creden.split() # Divide a entrada em nome de usuário e senha
if username and password:
    if processo.login(username, password):
        print("Login bem-sucedido!")
        opcao = input("Escolha uma opção:\n1. Criar novo objetivo\n2. Sair\n")
        if opcao == "1":
            processo.criar_objetivo()
    else:
        print("Falha no login. Por favor, verifique suas credenciais.")
print("--------------------------------")
