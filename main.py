# Modules and imports
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
import tkinter

# Window
window = tkinter.Tk()
window.geometry("400x300+800+400")
window.iconbitmap("images/bot.ico")
window.title("Chat Bot")
window.resizable(width=False, height=False)


# Title
title = tkinter.Label(window, text = "Hola mundo")
title.pack()

# Footer
footer = tkinter.Label(window, text = "Enrique Bazúa")
footer.pack(side = tkinter.BOTTOM)

window.mainloop()

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