from painel import PainelAeroporto 

def exibir_menu():
    #Exibe cabeçalho e as opções do menu no terminal.
    print("\n" + "=" * 54)
    print("    SISTEMA DE GERENCIAMENTO DE PAINEL DE VOOS")
    print("=" * 54)
    print("1. Cadastrar Novo Voo")
    print("2. Consultar Painel Completo de Decolagens")
    print("3. Consultar Voo específico pelo número")    
    print("4. Alterar Dados Cadastrais de um Voo")
    print("5. Avançar Status Operacionais de um Voo")
    print("6. Excluir Voo do Sistema")
    print("0. Sair do Sistema")
    print("=" * 54)

def main():
    #instancia o painel aeroportuário(Carrega os 8 voos automaticamente no __init__)]
    painel = PainelAeroporto()
    

    while True:
        exibir_menu()
        opcao = input("Escolha uma opção (0-6):").strip()

        # OPÇÃO 1: cadastrar um novo voo
        if opcao == "1":
            # Pede ao usuário cada dado do voo
            print("\n---CADASTRO DE NOVO VOO---")
            num = input("Número de Voo (EX: LA3456)")
            comp = input("Companhia Aérea:")
            emb = input ("Horário de Embarque (EX: 14:30)")
            sai = input("Horário de Saída (EX: 15:10)")
            dest = input("Destino")
            # cadastrar_voo valida os dados e devolve uma mensagem
            # de sucesso ou de erro, que é impressa na tela
            print(f"\n{painel.cadastrar_voo(num,comp,emb,sai,dest)}")

        #OPÇÃO 2: mostrar o painel completo com todos os voos
        elif opcao == "2":
            painel.exibir_painel()

        #OPÇÃO 3: consultar um voo específico pelo número
        elif opcao == "3":
            print("\n---CONSULTA DE VOO ESPECÍFICO---")
            num = input("Digite o número do voo:").strip()
             #buscar_voo devolve o voo encontrado ou None se não existir
            voo = painel.buscar_voo(num)    
            # Se encontrou o voo, mostra o cabeçalho e a linha dele
            if voo:
                print("\n" + "-" * 99)
                print(f"{'NÚMERO':<10} | {'COMPANHIA':<18} | {'EMBARQUE':<10} | {'SAÍDA':<10} | {'DESTINO':<18} | {'STATUS':<18}")
                print("-" * 99)
                print(voo)
                print("-" * 99)
             # Se não encontrou, avisa o usuário
            else:
             print(f"\n[ERRO] Voo {num.upper()} não localizado!")

        #OPÇÃO 4: alterar os dados cadastrais de um voo
        elif opcao == "4":
            print("\n---ALTERAÇÃO DE DADOS DO VOO---")
            num = input("Digite o número do voo para alterar:").strip()
            #Linha de teste: mostra os métodos do painel. Pode apagar.
            print([m for m in dir(painel) if not m.startswith("_")])
            voo = painel.buscar_voo(num)
            # Caso 1: o voo não existe
            if voo is None:
                print(f"\n[ERRO] Voo {num.upper()} não encontrado!")
            # Caso 2: regra de negócio, voo que já decolou não pode ser alterado
            elif voo.status == "DECOLOU":
                print(f"\n[BLOQUEIO] O voo {voo.numero_voo} já DECOLOU e não pode ser alterado!")
            # Caso 3: o voo existe e pode ser alterado
            else:
                print(f"Dados atuais {voo.companhia} | Embarque: {voo.horario_embarque} | Destino: {voo.destino}")
                nova_comp = input("Nova Companhia")
                novo_emb = input("Novo Embarque")
                nova_sai = input("Nova Saída")
                novo_dest = input("Novo Destino")
                print(f"\n{painel.alterar_voo(num, nova_comp, novo_emb, nova_sai, novo_dest)}")

        # OPÇÃO 5: avançar o status do voo
        # (PREVISTO -> CONFIRMADO -> EMBARQUE EM CURSO -> EMBARQUE ENCERRADO -> DECOLOU)
        elif opcao == "5":
            print("\n--AVANÇAR STATUS OPERACIONAL---")
            num = input("Digite o número do voo:").strip()
            voo = painel.buscar_voo(num)
            if voo:
                print(f"Status atual de {voo.numero_voo}: [{voo.status}]")
                if input("Avançar status? (S/N):").strip().upper() == "S":
                    print(f"\n{painel.avancar_status(num)}")
                else:
                    print(f"\nOperação cancelada.")
            else:
                print(f'\n[ERRO] Voo {num.upper()} não encontrado!')

        # OPÇÃO 6: excluir um voo do sistema
        elif opcao == "6":
            print("\n---EXCLUSÃO DE VOO---")
            num = input("Digite o número de voo para excluir:").strip()
            voo = painel.buscar_voo(num)
            # Se o voo existe, verifica a regra de exclusão
            if voo:
                # Regra de negócio: só pode excluir voo que já DECOLOU
                if voo.status != "DECOLOU":
                    print(f"\n[NEGADO] O voo {voo.numero_voo} está com status '{voo.status}'. Apenas voos 'DECOLOU' podem ser excluídos!")
                # Se decolou, pede confirmação antes de excl
                elif input(f"Confirma excluir o voo {voo.numero_voo}? (S/N):").strip().upper()=="S":
                    print(f'\n{painel.excluir_voo(num)}')
                # Se o usuário não confirmou, cancela
                else:
                    print("\nExclusão cancelada.")
                # Se o voo não existe, avisa o usuário
            else:
                print(f"\n[ERRO] Voo {num.upper()} não encontrado!")

        # OPÇÃO 0: encerrar o programa
        elif opcao == "0":
            print("\n===================================================")
            print("Sistema encerrado com sucesso. Até logo!")
            print("====================================================\n")
            break # sai do while True e termina o programa
            # Qualquer outra entrada (letras, números fora de 0-6, vazio)
        else:
            print("\n[ALERTA] Opção inválida! Escolha um número entre 0 e 6.")

if __name__ == "__main__":
    main()       
        