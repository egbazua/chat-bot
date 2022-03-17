# Modules and imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chat = ChatBot('cctmx')
while True:
    request = input('User: ')
    answer = chat.get_response(request)
    print('Bot: ', answer)