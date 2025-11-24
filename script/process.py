import calendar
import locale, re
from datetime import datetime, timedelta

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
        self.cal_str_colorido = self.cal_str.replace(f'{self.dia:2}', f'{RED}{self.dia:2}{RESET}')

    def mostrar_calendario_com_destaque(self, data_str, cor='\033[95m'):
        """✨ Exibe o calendário do mês da data fornecida, com o dia destacado na cor escolhida."""
        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            ano, mes, dia = data.year, data.month, data.day

            cal = calendar.TextCalendar(calendar.SUNDAY)
            cal_str = cal.formatmonth(ano, mes)

            RESET = '\033[0m'
            cal_str_colorido = cal_str.replace(f'{dia:2}', f'{cor}{dia:2}{RESET}')

            print("\n📌 Data agendada:", data.strftime('%A, %d de %B de %Y'))
            print(cal_str_colorido)

        except ValueError:
            print("⚠️ Formato inválido. Use DD/MM/AAAA.")

    def mostrar_calendario_manual(self, ano, mes, dias_destacados=None, cor="\033[92m"):
        """Mostra calendário com dias destacados em cor."""
        cal = calendar.TextCalendar(calendar.SUNDAY)
        cal_str = cal.formatmonth(ano, mes)

        if dias_destacados:
            for d in dias_destacados:
                padrao = rf"(?<!\d){d:2}(?!\d)"
                destaque = f"{cor}{d:2}\033[0m"
                cal_str = re.sub(padrao, destaque, cal_str)
        return cal_str

    def login(self, username, password):
        return username == "admin" and password == "admin123"

    def criar_objetivo(self):
        print("🎯 Que tipo de objetivo você gostaria de criar?")
        objetivo = input("Selecione:\n1️⃣ Tarefa diária\n2️⃣ Tarefa semanal\n3️⃣ Tarefa mensal\n👉 ")
        urgencia = int(input("🔥 Qual o nível de urgência dessa tarefa?\n   0-4: Adiável\n   5-7: Importante\n   8-10: Inadiável\n👉 "))

        if objetivo == "1" or objetivo.lower() == 'tarefa diária':
            self.criar_tarefa_diaria(urgencia)
        elif objetivo == "2" or objetivo.lower() == 'tarefa semanal':
            self.criar_tarefa_semanal(urgencia)
        elif objetivo == "3" or objetivo.lower() == 'tarefa mensal':
            self.criar_tarefa_mensal(urgencia)

    def criar_tarefa_diaria(self, urgencia):
        tarefa = input("📝 Que objetivo diário você gostaria de criar? ")
        data_str = input("📅 Digite a data da tarefa (DD/MM/AAAA): ")

        try:
            data = datetime.strptime(data_str, "%d/%m/%Y")
            cor = "\033[92m" if urgencia < 4 else "\033[93m" if urgencia <= 7 else "\033[91m"
            print("═" * 40)
            print(self.mostrar_calendario_manual(data.year, data.month, [data.day], cor))
            print(f"✅ Tarefa diária '{tarefa}' criada com urgência {urgencia} para {data.strftime('%d/%m/%Y')}.")
            print("═" * 40)
        except ValueError:
            print("⚠️ Data inválida. Use o formato DD/MM/AAAA.")

    def criar_tarefa_semanal(self, urgencia):
        tarefa = input("📝 Que objetivo semanal você gostaria de criar? ")
        data_str = input("📅 Digite a data de início da semana (DD/MM/AAAA): ")

        try:
            data_inicio = datetime.strptime(data_str, "%d/%m/%Y")
            ano, mes, dia = data_inicio.year, data_inicio.month, data_inicio.day
            fim = data_inicio + timedelta(days=6)
            dias_semana = [dia + i for i in range(7) if dia + i <= calendar.monthrange(ano, mes)[1]]

            cor = "\033[92m" if urgencia < 4 else "\033[93m" if urgencia <= 7 else "\033[91m"
            print("═" * 40)
            print(self.mostrar_calendario_manual(ano, mes, dias_semana, cor))
            print(f"✅ Tarefa semanal '{tarefa}' criada com urgência {urgencia} de {data_inicio.strftime('%d/%m/%Y')} até {fim.strftime('%d/%m/%Y')}.")
            print("═" * 40)
        except ValueError:
            print("⚠️ Data inválida. Use o formato DD/MM/AAAA.")

    def criar_tarefa_mensal(self, urgencia):
        tarefa = input("📝 Que objetivo mensal você gostaria de criar? ")
        mes = int(input("📅 Digite o mês da tarefa (1-12): "))
        ano = int(input("📅 Digite o ano da tarefa (ex: 2025): "))

        try:
            _, ultimo_dia = calendar.monthrange(ano, mes)
            dias_mes = list(range(1, ultimo_dia + 1))
            cor = "\033[92m" if urgencia < 4 else "\033[93m" if urgencia <= 7 else "\033[91m"
            print("═" * 40)
            print(self.mostrar_calendario_manual(ano, mes, dias_mes, cor))
            print(f"✅ Tarefa mensal '{tarefa}' criada com urgência {urgencia} para {calendar.month_name[mes]} de {ano}.")
            print("═" * 40)
        except:
            print("⚠️ Mês ou ano inválido.")

    def criar_tarefa_programada(self, urgencia):
        tarefa = input("📝 Que objetivo você gostaria de criar? ")
        data_str = input("📅 Para qual data você gostaria de agendar essa tarefa? (DD/MM/AAAA): ")

        try:
            cor = "\033[92m" if urgencia < 4 else "\033[93m" if urgencia <= 7 else "\033[91m"
            print("═" * 40)
            self.mostrar_calendario_com_destaque(data_str, cor)
            print(f"✅ Tarefa '{tarefa}' criada com urgência {urgencia} para {data_str}.")
            print("═" * 40)
        except ValueError:
            print("⚠️ Data inválida. Use o formato DD/MM/AAAA.")
