# Modules and imports
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

chat = ChatBot('cctmx')
trainer = ChatterBotCorpusTrainer(chat)
trainer.train("chatterbot.corpus.spanish.greetings")

while True:
    request = input('User: ')
    answer = chat.get_response(request)
    print('Bot: ', answer)