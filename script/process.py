import calendar
import locale
from datetime import datetime

class Processo:
    def __init__(self):
        # Definir localidade para português do Brasil
        locale.setlocale(locale.LC_TIME, 'pt_BR.UTF-8')

        # Data atual
        self.data_atual = datetime.now()
        self.ano = self.data_atual.year
        self.mes = self.data_atual.month
        self.dia = self.data_atual.day

        self.data_att = self.data_atual.strftime('%A, %d de %B de %Y')

        # Gera o calendário como string
        cal = calendar.TextCalendar(calendar.SUNDAY)
        self.cal_str = cal.formatmonth(self.ano, self.mes)

        # Adiciona cor ao dia atual
        RED = '\033[91m'
        RESET = '\033[0m'

        # Substitui o dia atual pela versão colorida
        self.cal_str_colorido = self.cal_str.replace(f'{self.dia:2}', f'{RED}{self.dia:2}{RESET}')
    
    def mostrar_calendario_com_destaque(self, data_str, cor='\033[95m'):
        #Exibe o calendário do mês da data fornecida, com o dia destacado na cor escolhida.
        #:param data_str: Data no formato 'DD/MM/AAAA'
        #:param cor: Código ANSI da cor (padrão: roxo)

        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            ano = data.year
            mes = data.month
            dia = data.day

            # Gera calendário do mês
            cal = calendar.TextCalendar(calendar.SUNDAY)
            cal_str = cal.formatmonth(ano, mes)

            # Aplica cor ao dia
            RESET = '\033[0m'
            cal_str_colorido = cal_str.replace(f'{dia:2}', f'{cor}{dia:2}{RESET}')

            # Exibe resultado
            print("\nData agendada:", data.strftime('%A, %d de %B de %Y'))
            print(cal_str_colorido)

        except ValueError:
            print("Formato inválido. Use DD/MM/AAAA.")

    def login(self, username, password):
        if username == "admin" and password == "admin123":
            return True
        else:
           return False
    
    def criar_objetivo(self):
        print("Que tipo de objetivo você gostaria de criar?")
        objetivo = input("Selecione o tipo de objetivo que deseja criar:\n1. Uma nova tarefa diária\n2. Uma nova tarefa semanal\n3. Uma nova tarefa mensal\n4. Uma nova tarefa com data programada\n")
        urgencia = int(input("Qual o nível de urgência dessa tarefa? Adiável(0-4), Importante(5-7) ou Inádiavel(8-10)\n"))

        if objetivo == "1" or objetivo == 'tarefa diária':
            self.criar_tarefa_diaria(urgencia)
        elif objetivo == "2" or objetivo == 'tarefa semanal':
            self.criar_tarefa_semanal(urgencia)
        elif objetivo == "3" or objetivo == 'tarefa mensal':
            self.criar_tarefa_mensal(urgencia)
        elif objetivo == "4" or objetivo == 'tarefa com data programada':
            self.criar_tarefa_programada(urgencia)
    
    def criar_tarefa_diaria(self, urgencia):
        tarefa = input("Que objetivo diário você gostaria de criar?")
        print("--------------------------------")
        print(self.cal_str_colorido) # Exibe o calendário com o dia atual destacado
        print(f"Tarefa diária '{tarefa}' criada com urgência {urgencia}.")
        if urgencia >= 4:
            print("Te avisaremos um dia antes de seu prazo!")
        elif urgencia >= 5 and urgencia <= 7:
            print("Te avisaremos durante 3 dias antes de seu prazo!")
        elif urgencia > 7:
            print("Te avisaremos durante uma semana antes de seu prazo!")
        print("--------------------------------")


    def criar_tarefa_semanal(self, urgencia):
        pass

    def criar_tarefa_mensal(self, urgencia):
        pass

    def criar_tarefa_programada(self, urgencia):
        tarefa = input("Que objetivo diário você gostaria de criar?")
        print("--------------------------------")
        print(self.cal_str_colorido) # Exibe o calendário com o dia atual destacado
        data = input("Para qual data você gostaria de agendar essa tarefa? (DD/MM/AAAA)\n")
        if data:
            # Exibe o calendário com o dia escolhido destacado
            self.mostrar_calendario_com_destaque(data)
            print(f"Tarefa diária '{tarefa}' criada com urgência {urgencia} para a data {data}.")
            if urgencia >= 4:
                print("Te avisaremos um dia antes de seu prazo!")
            elif urgencia >= 5 and urgencia <= 7:
                print("Te avisaremos durante 3 dias antes de seu prazo!")
            elif urgencia > 7:
                print("Te avisaremos durante uma semana antes de seu prazo!")
            print("--------------------------------")