import os
import re
import sys
from time import sleep
from colorama import init, Fore, Style
import google.generativeai as genai

init(autoreset=True)

# Variables for organization:
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

# CONFIGURATION:
API_KEY = ""  # SUA-CHAVE-DE-API / YOUR-API-KEY

# CONFIGURING THE CHATBOT:
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel('gemini-pro')
chat = model.start_chat(history=[])

# Now let's start a chat between the user and the bot
clear_terminal()
sleep(1)
print(f"{notice}The conversation history will be saved in {Fore.WHITE}historic.json")
sleep(1)
print(f"{notice}Type {Fore.WHITE}'exit' {Fore.RESET}to end the conversation whenever you want.\n")
sleep(1)

while True:
    # We'll use colorama for better visualization
    user_message = input(f"{Style.BRIGHT + Fore.WHITE}You: {Fore.WHITE}")
    if user_message.lower() == 'exit':
        sleep(1.1)
        print(f"{notice}{Style.BRIGHT + Fore.WHITE}Ending the conversation.")
        sys.exit()
    else:
        try:
            msg = chat.send_message(f"{user_message}")
            pdf_input = ""
        except:
            print(f"{Style.BRIGHT + Fore.RED}Error, maybe the AI didn't understand your prompt, try again...")
            sleep(3)
            clear_terminal()
            continue

        # Print the AI's response:
        try:
            response = msg.text
        except:
            response = ''.join(x for x in msg.parts)

        response = f"{Style.BRIGHT + Fore.YELLOW}AI: {Fore.GREEN}{response}"
        for _ in range(len(response)):
            response = response.replace("**", f"{Style.BRIGHT + Fore.YELLOW}", 1)
            response = response.replace("**", f"{Fore.GREEN}", 1)
            response.replace("*", "-")
            response = re.sub('__*', '', response)
            response = re.sub(r'```.*', '```', response)
            response = response.replace("```", f"{Style.BRIGHT + Fore.BLUE}", 1)
            response = response.replace("```", f"{Fore.GREEN}", 1)
            response = response.replace('`', f"{Fore.WHITE}", 1)
            response = response.replace("`", f"{Fore.GREEN}", 1)

            numbers = [int(x) for x in range(10)]
            for number in numbers:
                response.replace(str(number), f'{Style.BRIGHT}{number}')

        print(response)
        sleep(0.3)
        with open('historic.json', 'w', encoding='utf-8') as file:
            file.write(str(chat.history,))
        file.close()