from script.process import Processo  # Importa a classe Processo do módulo process

# Inicia o sistema OrgaMe
processo = Processo()  # 🧠 Cria uma instância da classe Processo

print("═" * 40)
print("🎯 Bem-vindo(a) ao OrgaMe — Seu organizador de metas!")
print("🔐 Faça login para começar sua jornada de produtividade.")
print("═" * 40)

# Coleta credenciais
creden = input("👤 Digite seu usuário e senha separados por espaço: ")
username, password = creden.split()  # Divide a entrada em nome de usuário e senha

# 🔍 Verifica login
if username and password:
    if processo.login(username, password):
        print("✅ Login bem-sucedido! Seja bem-vindo(a),", username)
        print("📌 Escolha uma opção abaixo:")
        opcao = input("📝 1. Criar novo objetivo\n❌ 2. Sair\n ")

        if opcao == "1":
            processo.criar_objetivo()
        elif opcao == "2":
            print("👋 Até logo! Volte sempre ao OrgaMe.")
        else:
            print("⚠️ Opção inválida. Tente novamente.")
    else:
        print("❌ Falha no login. Verifique suas credenciais e tente novamente.")
else:
    print("⚠️ Usuário ou senha não informados.")

print("═" * 40)
