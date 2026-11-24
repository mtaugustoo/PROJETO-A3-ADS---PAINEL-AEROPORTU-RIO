from Voo import Voo
class PainelAeroporto:
    def __init__(self):
        self.voos = [] #método foi criado, lista está vazia, pronta para receber voos depois.
        self.carregar_dados_iniciais()

    def carregar_dados_iniciais(self): 
        self.cadastrar_voo("LA3456", "LATAM", "14:30", "15:10", "Rio de Janeiro") 
        self.cadastrar_voo("GL1208", "GOL", "15:00", "15:45", "Salvador") 
        self.cadastrar_voo("AZ4510", "AZUL", "16:15", "17:00", "Curitiba")
        self.cadastrar_voo("TP0088", "TAP", "18:20", "19:10", "Lisboa")
        self.cadastrar_voo("AD2400", "AZUL", "19:30", "20:15", "Florianópolis") 
        self.cadastrar_voo( "AR1240", "Aerolineas", "20:00", "20:50", "Buenos Aires" ) 
        self.cadastrar_voo("AA0950","American Airlines","21:15","22:05","Miami") 
        self.cadastrar_voo("AF0457", "Air France", "22:45", "23:40", "Paris")

    def buscar_voo(self, numero_voo: str) : #Localiza um voo pelo número.
        for voo in self.voos: 
            if voo.numero_voo.upper() == numero_voo.upper(): 
               # Percorre os voos e verifica se o número é igual ao buscado (sem diferenciar maiúsculas de minúsculas)
              return voo  # -> devolve o voo e encerra o método na hora.
        return None      # -> caso aconteça de não encontrar nenhum voo.

    def cadastrar_voo(self, numero_voo: str, companhia: str, horario_embarque: str, horario_saida: str, destino: str) -> str:
        #Cadastra um novo voo com status inicial "PREVISTO", valida se o número de voo já existe para evitar duplicidade.
        #Validação 1: Unicidade do número do Voo
        if self.buscar_voo(numero_voo) is not None:
            return "[ERRO] Falha no cadastro: Já existe um voo cadastrado com esse número!" 
        #Validação 2: Campos Obrigatórios não vazios
        if not numero_voo or not companhia or not horario_embarque or not horario_saida or not destino:
            return "[ERRO] falha no cadastro: todos os campos são obrigatórios"
        #Instanciando o novo voo
        novo_voo = Voo(numero_voo.upper(), companhia, horario_embarque, horario_saida , destino)
        #Adiciona na lista em memória RAM
        self.voos.append(novo_voo)
        return f"[OK] Voo {novo_voo.numero_voo} cadastrado com sucesso! Status inicial: PREVISTO"

            #               Exibe todos os voos cadastrados no formato de painel aeroportuário.
            #Se a lista de voos estiver vazia, mostra uma mensagem e encerra o método
    def exibir_painel(self):
        
        if not self.voos:
            print("\n" + "-" * 99)
            print("                           NENHUM VOO CADASTRADO NO PAINEL")
            print("-" * 99)
            return  # sai do método, não executa o resto
            # Se houver voos, imprime o cabeçalho do painel
        print("\n" + "=" * 99)
        print("                               PAINEL DE DECOLAGEM")
        print("=" * 99)
        # Imprime os títulos das colunas, cada um com largura fixa e alinhado à esquerd
        print(f"{'NÚMERO':<10} | {'COMPANHIA':<18} | {'EMBARQUE':<10} | {'SAÍDA' :<10} | {'DESTINO':<18} | {'STATUS':<18}")
        print("-" * 99)
        #Percorre a lista de voos e imprime cada um
        for voo in self.voos:
            print(voo)
        #Linha final para fechar o painel
        print("=" * 99 + "\n")

     
    def alterar_voo(self, numero_voo: str, nova_companhia: str, novo_embarque: str, nova_saida: str, novo_destino: str) -> str:
        #Atualizando as informações cadastrais de um voo.
        #REGRA DE NEGÓCIO: Não permite alterar voos com status: "DECOLOU".
        voo = self.buscar_voo(numero_voo)
        if voo is None:
            return "[ERRO] Falha: Voo inexistente!"

        #Trava de segurança: Voo decolado não pode ter dados alterados
        if voo.status == "DECOLOU":
            return f"[ERRO] Operação negada: O voo {voo.numero_voo} já DECOLOU e não pode ser alterado!"

        #Atualiza os dados cadastrais 
        voo.companhia = nova_companhia
        voo.horario_embarque = novo_embarque 
        voo.horario_saida = nova_saida
        voo.destino = novo_destino
        return f"[OK] Dados do voo {voo.numero_voo} atualizado com sucesso!"

    def avancar_status(self, numero_voo: str) -> str:
        # Avança o status do voo respeitando a sequência:
        # PREVISTO -> CONFIRMADO -> EMBARQUE EM CURSO -> EMBARQUE ENCERRADO -> DECOLOU
        voo_encontrado = self.buscar_voo(numero_voo)
        if voo_encontrado is None:
            return "[ERRO] Falha: Voo inexistente!"

        sequencia_status = {
        "PREVISTO": "CONFIRMADO",
        "CONFIRMADO": "EMBARQUE EM CURSO",
        "EMBARQUE EM CURSO": "EMBARQUE ENCERRADO",
        "EMBARQUE ENCERRADO": "DECOLOU"
        }
        status_atual = voo_encontrado.status
        if status_atual in sequencia_status:
            proximo = sequencia_status[status_atual]
            voo_encontrado.status = proximo
            return f"[STATUS] Status do voo {voo_encontrado.numero_voo} alterado de '{status_atual}' para '{proximo}'!"
        else:
            return f"[ALERTA] O voo {voo_encontrado.numero_voo} já está no status final ({status_atual}) e não pode avançar."

    def excluir_voo(self, numero_voo: str) -> str:
        # Remove um voo da memória.
        # Regra: Um voo só pode ser excluído se o seu status atual for 'DECOLOU'
        voo = self.buscar_voo(numero_voo)
        if voo is None:
            return "[ERRO] Falha na exclusão: Voo inexistente!"
        #Trava de Segurança de Exclusão (REGRA)
        if voo.status != "DECOLOU":
            return f"[ERRO] Exclusão negada: O voo {voo.numero_voo} está em '{voo.status}' Apenas voos 'DECOLOU' podem ser excluídos"
        #Remove o objeto lista da memória RAM
        self.voos.remove(voo)
        return f"[REMOVIDO] Voo `{numero_voo.upper()}' removido do sistema com sucesso!"
        