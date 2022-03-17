# Modules and imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer

chat = ChatBot('Venado')
talk = ['Hola', '¿Qué tal?', 'Tengo una pregunta', 'Si, dime',
        'La comida en méxico es buena?', 'Si, es deliciosa?', 
        '¿Qué me recomiendas?', 'Tamales', 'Muchas gracias']
trainer = ListTrainer(chat)
trainer.train(talk)

while True:
    request = input('User: ')
    answer = chat.get_response(request)
    print('Bot: ', answer)