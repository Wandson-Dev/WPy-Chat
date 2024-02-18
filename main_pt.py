import os
import re
import sys
from time import sleep
from colorama import init, Fore, Style
import google.generativeai as genai

init(autoreset=True)

# Variáveis para organização:
aviso = f"{Style.BRIGHT + Fore.BLUE}[ ! ] {Fore.RESET}"

def limpar_terminal():
    sistema_operacional = os.name
    try:
        if sistema_operacional == 'posix':
            os.system('clear')
        elif sistema_operacional == 'nt':
            os.system('cls')
        else:
            os.system('clear' if os.name == 'posix' else 'cls')
    except:
        print("\n")

# CONFIGURAÇÃO:
API_KEY = "SUA-CHAVE-DE-API"

# CONFIGURANDO O CHATBOT:
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Agora vamos iniciar uma chat entre o usuário e o bot
limpar_terminal()
sleep(1)
print(f"{aviso}O histórico dessa conversa será salvo em {Fore.WHITE}historic.json")
sleep(1)
print(f"{aviso}Digite {Fore.WHITE}'exit' {Fore.RESET}para finalizar a conversa quando quiser.\n")
sleep(1)

while True:
    # Usaremos colorama para melhorar a visualização
    mensagem_usuario = input(f"{Style.BRIGHT + Fore.WHITE}Você: {Fore.WHITE}")
    if mensagem_usuario.lower() == 'exit':
        sleep(1.1)
        print(f"{aviso}{Style.BRIGHT + Fore.WHITE}Encerrando a conversa.")
        sys.exit()
    else:
        try:
            msg = chat.send_message(f"{mensagem_usuario}")
            pdfinput = ""
        except:
            print(f"{Style.BRIGHT + Fore.RED}Erro, talvez a IA não tenha entendido seu prompt, tente novamente...")
            sleep(3)
            limpar_terminal()
            continue
        
        # Printar a resposta da IA:
        try:
            resposta = msg.text
        except:
            resposta = ''.join(x for x in msg.parts)

        resposta = f"{Style.BRIGHT + Fore.YELLOW}IA: {Fore.GREEN}{resposta}"
        for _ in range(len(resposta)):
            resposta = resposta.replace("**", f"{Style.BRIGHT + Fore.YELLOW}", 1)
            resposta = resposta.replace("**", f"{Fore.GREEN}", 1)
            resposta.replace("*", "-")
            resposta = re.sub('__*', '', resposta)
            resposta = re.sub(r'```.*', '```', resposta)
            resposta = resposta.replace("```", f"{Style.BRIGHT + Fore.BLUE}", 1)
            resposta = resposta.replace("```", f"{Fore.GREEN}", 1)
            resposta = resposta.replace('`', f"{Fore.WHITE}", 1)
            resposta = resposta.replace("`", f"{Fore.GREEN}", 1)
            
            numeros = [int(x) for x in range(10)]
            for numero in numeros:
                resposta.replace(str(numero), f'{Style.BRIGHT}{numero}')

        print(resposta)
        sleep(0.3)
        with open('historic.json', 'w', encoding='utf-8') as arq:
        	arq.write(str(chat.history,))
        arq.close()