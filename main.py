tarefas = []

def mostrar_menu():
    print("\n--- Gerenciador de Tarefas ---")
    print("1 - Adicionar tarefa")
    print("2 - Listar tarefas")
    print("3 - Remover tarefa")
    print("0 - Sair")

def adicionar_tarefa():
    nome = input("Digite a tarefa: ")
    prioridade = input("Prioridade (Alta / Média / Baixa): ")
    tarefas.append({"nome": nome, "prioridade": prioridade})
    print("Tarefa adicionada com sucesso!")

def listar_tarefas():
    if not tarefas:
        print("Nenhuma tarefa cadastrada.")
    else:
        for i, tarefa in enumerate(tarefas):
            print(f"{i + 1} - {tarefa['nome']} | Prioridade: {tarefa['prioridade']}")

def remover_tarefa():
    listar_tarefas()
    try:
        indice = int(input("Digite o número da tarefa a remover: ")) - 1
        tarefas.pop(indice)
        print("Tarefa removida com sucesso!")
    except:
        print("Opção inválida.")

while True:
    mostrar_menu()
    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        adicionar_tarefa()
    elif opcao == "2":
        listar_tarefas()
    elif opcao == "3":
        remover_tarefa()
    elif opcao == "0":
        print("Saindo do sistema...")
        break
    else:
        print("Opção inválida.")

