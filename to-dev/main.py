#lib
import google.generativeai as genai

#your api-key. get in https://aistudio.google.com/app/apikey
API_KEY = ""

#config
genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

#chat
while True:
	you = input("Você: ")
	try:
		response = chat.send_message(you)
	except:
		response = "Error, try again..."
		continue
		
	try:
	   response =  response.text
	except:
	   response = ''.join(x for x in msg.parts)
	
	print(f"IA: {response}")