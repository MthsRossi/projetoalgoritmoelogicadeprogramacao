# Sistema de Gestão de Peças, Qualidade e Armazenamento

pecas = []
caixas_fechadas = []
capacidade_caixa = 10


def validar_peca(peso, cor, comprimento):
    motivos = []

    if peso < 95 or peso > 105:
        motivos.append("Peso fora do padrão")

    if cor.lower() not in ["azul", "verde"]:
        motivos.append("Cor inválida")

    if comprimento < 10 or comprimento > 20:
        motivos.append("Comprimento fora do padrão")

    if len(motivos) == 0:
        return True, ["Peça aprovada"]
    else:
        return False, motivos


def atualizar_caixas():
    global caixas_fechadas

    pecas_aprovadas = [peca for peca in pecas if peca["status"] == "Aprovada"]

    caixas_fechadas = []
    caixa_atual = []

    for peca in pecas_aprovadas:
        caixa_atual.append(peca)

        if len(caixa_atual) == capacidade_caixa:
            caixas_fechadas.append(caixa_atual)
            caixa_atual = []


def cadastrar_peca():
    print("\n=== CADASTRAR NOVA PEÇA ===")

    id_peca = input("Digite o ID da peça: ").strip()

    for peca in pecas:
        if peca["id"] == id_peca:
            print("Erro: já existe uma peça cadastrada com esse ID.")
            return

    try:
        peso = float(input("Digite o peso da peça (g): "))
        cor = input("Digite a cor da peça: ").strip().lower()
        comprimento = float(input("Digite o comprimento da peça (cm): "))
    except ValueError:
        print("Erro: peso e comprimento devem ser números.")
        return

    aprovada, motivos = validar_peca(peso, cor, comprimento)

    nova_peca = {
        "id": id_peca,
        "peso": peso,
        "cor": cor,
        "comprimento": comprimento,
        "status": "Aprovada" if aprovada else "Reprovada",
        "motivos": motivos
    }

    pecas.append(nova_peca)

    atualizar_caixas()

    print("\nPeça cadastrada com sucesso.")
    print(f"Status: {nova_peca['status']}")
    print("Motivo(s):", ", ".join(nova_peca["motivos"]))


def listar_pecas():
    print("\n=== LISTAGEM DE PEÇAS ===")

    if len(pecas) == 0:
        print("Nenhuma peça cadastrada.")
        return

    print("\n1. Listar aprovadas")
    print("2. Listar reprovadas")
    print("3. Listar todas")
    opcao = input("Escolha uma opção: ").strip()

    encontrou = False

    for peca in pecas:
        if opcao == "1" and peca["status"] != "Aprovada":
            continue
        if opcao == "2" and peca["status"] != "Reprovada":
            continue
        if opcao not in ["1", "2", "3"]:
            print("Opção inválida.")
            return

        encontrou = True
        print("\n-----------------------------")
        print(f"ID: {peca['id']}")
        print(f"Peso: {peca['peso']} g")
        print(f"Cor: {peca['cor']}")
        print(f"Comprimento: {peca['comprimento']} cm")
        print(f"Status: {peca['status']}")
        print(f"Motivo(s): {', '.join(peca['motivos'])}")

    if not encontrou:
        print("Nenhuma peça encontrada nessa categoria.")


def remover_peca():
    print("\n=== REMOVER PEÇA CADASTRADA ===")

    if len(pecas) == 0:
        print("Nenhuma peça cadastrada.")
        return

    id_peca = input("Digite o ID da peça que deseja remover: ").strip()

    for i, peca in enumerate(pecas):
        if peca["id"] == id_peca:
            del pecas[i]
            atualizar_caixas()
            print("Peça removida com sucesso.")
            return

    print("Peça não encontrada.")


def listar_caixas_fechadas():
    print("\n=== CAIXAS FECHADAS ===")

    if len(caixas_fechadas) == 0:
        print("Nenhuma caixa foi fechada ainda.")
        return

    for i, caixa in enumerate(caixas_fechadas, start=1):
        print(f"\nCaixa {i} - Total de peças: {len(caixa)}")
        for peca in caixa:
            print(f"  - ID da peça: {peca['id']}")


def gerar_relatorio():
    print("\n=== RELATÓRIO FINAL ===")

    total_aprovadas = 0
    total_reprovadas = 0
    motivos_reprovacao = {}

    for peca in pecas:
        if peca["status"] == "Aprovada":
            total_aprovadas += 1
        else:
            total_reprovadas += 1
            for motivo in peca["motivos"]:
                if motivo in motivos_reprovacao:
                    motivos_reprovacao[motivo] += 1
                else:
                    motivos_reprovacao[motivo] = 1

    pecas_aprovadas = [peca for peca in pecas if peca["status"] == "Aprovada"]
    caixa_em_andamento = len(pecas_aprovadas) % capacidade_caixa

    print(f"Total de peças cadastradas: {len(pecas)}")
    print(f"Total de peças aprovadas: {total_aprovadas}")
    print(f"Total de peças reprovadas: {total_reprovadas}")
    print(f"Quantidade de caixas fechadas: {len(caixas_fechadas)}")
    print(f"Peças na caixa atual (ainda não fechada): {caixa_em_andamento}")

    print("\nMotivos de reprovação:")
    if len(motivos_reprovacao) == 0:
        print("Nenhuma peça reprovada.")
    else:
        for motivo, quantidade in motivos_reprovacao.items():
            print(f"- {motivo}: {quantidade} peça(s)")


def menu():
    while True:
        print("\n========== MENU ==========")
        print("1. Cadastrar nova peça")
        print("2. Listar peças aprovadas/reprovadas")
        print("3. Remover peça cadastrada")
        print("4. Listar caixas fechadas")
        print("5. Gerar relatório final")
        print("0. Sair")

        opcao = input("Escolha uma opção: ").strip()

        if opcao == "1":
            cadastrar_peca()
        elif opcao == "2":
            listar_pecas()
        elif opcao == "3":
            remover_peca()
        elif opcao == "4":
            listar_caixas_fechadas()
        elif opcao == "5":
            gerar_relatorio()
        elif opcao == "0":
            print("Encerrando o programa...")
            break
        else:
            print("Opção inválida. Tente novamente.")


menu()