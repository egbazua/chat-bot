# Modules and imports
from cgitb import text
from tkinter import ttk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from tkinter import *

# Main Function
def main():

    # ChatBot
    chat = ChatBot('Venado')
    talk = ['Hola', '¿Qué tal?', 'Tengo una pregunta', 'Si, dime',
            'La comida en méxico es buena?', 'Si, es deliciosa?', 
            '¿Qué me recomiendas?', 'Tamales', 'Muchas gracias']
    trainer = ListTrainer(chat)
    trainer.train(talk)

    # Window
    window = Tk()
    window.geometry("400x300+800+400")
    window.iconbitmap("images/bot.ico")
    window.title("Chat Bot")
    window.resizable(width=False, height=False)

    # Title
    title = Label(window, text = "Platica conmigo", font = ('Times 18'))
    title.pack()

    # Frame
    frame = Frame(window, width=320, height=215, highlightbackground="black", highlightthickness=1)
    frame.pack()
    frame.config(bg="white")

    # Footer
    """ footer = tkinter.Label(window, text = "Enrique Bazúa")
    footer.pack(side = tkinter.BOTTOM) """

    # Buttom
    button = ttk.Button(text = "Enviar mensaje", command = startChat)
    button.pack(side = BOTTOM)

    # TextBox
    textbox = ttk.Entry()
    textbox.pack(side = BOTTOM)

    window.mainloop()

def startChat():
    print("Hola mundo")
    
# Calling main Function
main()

""" while True:
    request = input('User: ')
    answer = chat.get_response(request)
    print('Bot: ', answer) """