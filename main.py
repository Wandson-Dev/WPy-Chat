import os
import re
import sys
from time import sleep
from colorama import init, Fore, Style
import google.generativeai as genai

init(autoreset=True)

# Obter chave da API
with open('api-key', 'r') as keyGet:
    key = keyGet.read()

# Variáveis para organização:
notice = f"{Style.BRIGHT + Fore.BLUE}[ ! ] {Fore.RESET}"  # [ ! ] / [ ! ]

def clear_terminal():
    operating_system = os.name
    try:
        if operating_system == 'posix':
            os.system('clear')
        elif operating_system == 'nt':
            os.system('cls')
        else:
            os.system('clear' if os.name == 'posix' else 'cls')
    except:
        print("\n")

# CONFIGURAÇÃO:
API_KEY = key  # SUA-CHAVE-DE-API / YOUR-API-KEY

# CONFIGURANDO O CHATBOT:
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Agora vamos iniciar uma conversa entre o usuário e o bot
clear_terminal()
sleep(1)
print(f"{notice}O histórico da conversa será salvo em {Fore.WHITE}historic.json")
sleep(1)
print(f"{notice}Digite {Fore.WHITE}'exit' {Fore.RESET}para terminar a conversa a qualquer momento.\n")
sleep(1)

while True:
    # Vamos usar colorama para melhor visualização
    user_message = input(f"{Style.BRIGHT + Fore.WHITE}Você: {Fore.WHITE}")
    if user_message.lower() == 'exit':
        sleep(1.1)
        print(f"{notice}{Style.BRIGHT + Fore.WHITE}Finalizando a conversa.")
        sys.exit()
    else:
        try:
            msg = chat.send_message(f"{user_message}")
            pdf_input = ""
        except:
            print(f"{Style.BRIGHT + Fore.RED}Erro, talvez a IA não tenha entendido seu prompt, tente novamente...")
            sleep(3)
            clear_terminal()
            continue

        # Exibir a resposta da IA:
        try:
            response = msg.text
        except:
            response = ''.join(x for x in msg.parts)

        response = f"{Style.BRIGHT + Fore.YELLOW}IA: {Fore.GREEN}{response}"
        
        for _ in range(len(response)):
            response = re.sub(r'\*\*(.*?)\*\*', f'{Style.BRIGHT + Fore.YELLOW}\\1{Style.RESET_ALL}', response)
            response = re.sub(r'__(.*?)__', f'{Style.BRIGHT + Fore.CYAN}\\1{Style.RESET_ALL}', response)
            response = re.sub(r'`(.*?)`', f'{Fore.WHITE}\\1{Style.RESET_ALL}', response)
            response = re.sub(r'```(\w+)', f'{Style.BRIGHT + Fore.BLUE}```\\1', response)
            response = re.sub(r'```', f'{Style.BRIGHT + Fore.GREEN}```', response)

            numbers = [int(x) for x in range(10)]
            for number in numbers:
                response.replace(str(number), f'{Style.BRIGHT}{number}')

        print(response)
        sleep(0.3)
        with open('historic.json', 'w', encoding='utf-8') as file:
            file.write(str(chat.history,))
        file.close()
