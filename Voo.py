# PROJETO A3 (ADS) - PAINEL AEROPORTUÁRIO
# Arquivo: voo.py | Página 1: Classe Voo (Estrutura do Objeto)
# Observação: Versão preliminar em Python antes da implementação em Java

class Voo:
    def __init__(self, numero_voo: str, companhia: str, horario_embarque: str, horario_saida: str, destino: str):
        #Identificador único de registro
        self.numero_voo = numero_voo
        #Empresa área responsável pelo Voo
        self.companhia = companhia
        #Horário previsto para início de embarque
        self.horario_embarque = horario_embarque
        #Horário previsto para desembarque do Voo
        self.horario_saida = horario_saida
        #Cidade destino
        self.destino = destino
        #o status operacional não se encontra no parâmetro acima () pelo fato de iniciar automaticamente como PREVISTO - Não existe uma opção do usuário escolher o status inicial no momento de cadastro
        self.status = "PREVISTO"

def __str__(self): # -> __str__ método para criar um painel/interface para uma experiência melhor para o usuário.
    return  ( 
        # f-string: formata o texto, inserindo variáveis entre {} e alinhando a coluna
    f"{self.numero_voo:<10} | " 
    f"{self.companhia:<15} | "
    f"{self.horario_embarque:<10} | "
    f"{self.horario_saida:<10} | "
    f"{self.destino:<18} | "
    f"{self.status}"
    )
