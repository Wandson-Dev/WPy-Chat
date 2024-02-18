import google.generativeai as genai

API_KEY = ""

genai.configure(api_key=API_KEY)
model = genai.GenerativeModel("gemini-pro")
chat = model.start_chat(history=[])

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