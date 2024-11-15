from devices import devices_list

user_devices = []

def verify_number(number, limit):
    if number > limit:
        raise ValueError()
    
def secutiry_input(message):
    while True:
        try:
            input_device = float(input(message))
            verify_number(input_device, len(devices_list) + 1)
            return input_device
        except ValueError:
            print("Digite um número válido")

def init():
    print("Bem vindo a calculadora de 'Quantos Watts?'!")
    menu()

def menu():
    print("1 - Calculo semanal de consumo")
    print("2 - Sair")

    input_menu = input("Digite a opção desejada: ")

    if input_menu == "1":
        calculo_semanal()
    elif input_menu == "2":
        print("Até mais!")


def calculo_semanal():
    print("Calculo semanal, insira todos aparelhos que você usa durante a semana")

    print("Aparelhos disponíveis:")

    while True:

        for i in range(len(devices_list)):
            device = devices_list[i]
            print(f"{i + 1} - {device['name']} - {device['wattsPerHour']}W")
        
        print(f"{len(devices_list) + 1} - Encerrar")

        input_device = secutiry_input("Digite o número do aparelho que deseja adicionar: ")


        if input_device == len(devices_list) + 1:    
            if user_devices == []:
                print("Você não adicionou nenhum aparelho")
                break
            else:
                consumption_history()    
                break
        else:
            deviceItem = devices_list[int(input_device) - 1]

            hours = secutiry_input("Quantas horas por dia você usa esse aparelho? ")
            day = secutiry_input("Quantos dias por semana você usa esse aparelho? ")
            
            weekly_consumption = deviceItem['wattsPerHour'] * hours * day

            device = {
                "name": deviceItem['name'],
                "wattsPerHour": deviceItem['wattsPerHour'],
                "hours": hours,
                "days": day,
                "weekly_consumption": weekly_consumption,
                "monthly_consumption": weekly_consumption * 4
            }

            user_devices.append(device)
            print(f"{device['name']} adicionado com sucesso!")

        print("Mais algum aparelho?")

    menu()

def consumption_history():
    file = open("consumption_history.txt", "w")

    text = ""

    text += "Historico de consumo\n"

    for key in user_devices[0].keys():
        text += f"{key:<20}|"

    text += "\n"


    for device in user_devices:
        for key in device.keys():
            text += f"{device[key]:<20}|"

        text += "\n"


    file.write(text)

    file.close()
    print("Histórico de consumo salvo com sucesso!")


init()