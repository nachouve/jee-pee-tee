import sys
import dotenv

#from revChatGPT.revChatGPT import Chatbot
from chatbot import Chatbot
from utils import load_config

dotenv.load_dotenv()

config = load_config()
chatgpt = Chatbot(config)
chatgpt.refresh_session()

while True:
    text = input("You: ")
    if text.lower() == "stop":
        break
    response = chatgpt.get_chat_response(text)
    print(f"ChatGPT: {response}")