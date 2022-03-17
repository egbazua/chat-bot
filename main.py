# Modules and imports
from cgitb import text
from multiprocessing.sharedctypes import Value
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

    # Variables
    message = StringVar()

    # Title
    title = Label(window, text = "Platica conmigo", font = ('Times 18'))
    title.pack()

    # Frame
    frame = Frame(window, width=320, height=205, highlightbackground="black", highlightthickness=1)
    frame.pack()
    frame.config(bg="white")

    # Footer
    """ footer = tkinter.Label(window, text = "Enrique Bazúa")
    footer.pack(side = tkinter.BOTTOM) """

    # User Messages
    userMessage = Label(frame, text = "", font = ('Arial 10'))
    """ userMessage.pack(side = RIGHT) """
    userMessage.place(x=250, y=170)

    # Bot Messages
    botTitle = Label(frame, text="ChatBot:", font=('Arial 10'), bg="white", fg="red")
    botTitle.place(x=10, y=10)

    botMessage = Label(frame, text = "", font = ('Arial 10'), bg="white")
    """ botMessage.pack(side = LEFT) """
    botMessage.place(x=10, y=40)

    # Button
    button = ttk.Button(text = "Enviar mensaje", command = lambda: startChat(window, textbox, userMessage, chat, botMessage))
    button.pack(side = BOTTOM, pady=5)

    # TextBox
    textbox = ttk.Entry(textvariable = message)
    textbox.pack(side = BOTTOM)

    window.mainloop()

# Start Chat Button
def startChat(window, textbox, userMessage, chat, botMessage):
    value = textbox.get()
    userMessage["text"] = value
    
    request = value
    answer = chat.get_response(request)
    botMessage["text"] = answer


# Calling main Function
main()

""" while True:
    request = input('User: ')
    answer = chat.get_response(request)
    print('Bot: ', answer) """