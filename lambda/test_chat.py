import sys
import dotenv

#from revChatGPT.revChatGPT import Chatbot
from chatbot import Chatbot
from utils import load_config

dotenv.load_dotenv()

if len(sys.argv) != 2:
    print("You must provide text")
    sys.exit(1)

text = sys.argv[1]

print(f"Asking ChatGPT '{text}'")

config = load_config()
chatgpt = Chatbot(config)
chatgpt.refresh_session()
response = chatgpt.get_chat_response(text)

print(response)
