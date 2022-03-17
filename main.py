# Modules and imports
from cgitb import text
from multiprocessing.sharedctypes import Value
from tkinter import ttk
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from chatterbot.trainers import ChatterBotCorpusTrainer
from tkinter import *

# Main Function
def main():

    # ChatBot
    chat = ChatBot('Venado')
    trainer = ChatterBotCorpusTrainer(chat)
    trainer.train(
        "chatterbot.corpus.spanish.conversations",
        "chatterbot.corpus.spanish.greetings",
        "chatterbot.corpus.spanish.trivia",
        )

    # Manual words
    """ talk = ['Hola', '¿Qué tal?', 'Tengo una pregunta', 'Si, dime',
            'La comida en méxico, ¿es buena?', 'Si, ¿es deliciosa?', 
            '¿Qué me recomiendas?', 'Tamales', 'Muchas gracias'] """
    """  trainer = ListTrainer(chat) """
    
    """ trainer.train(talk) """

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

    # Images
    """ botCanvas = Canvas(frame, width=50, height=50)
    botImage = PhotoImage(file="images/bot.png")
    botCanvas.create_image(20, 20, anchor=NW, image=botImage) """

    # User Messages
    userTitle = Label(frame, text="Usuario:", font=('Arial 10'), bg="white", fg="blue")
    userTitle.place(x=10, y=145)

    userMessage = Label(frame, text = "", font = ('Arial 10'), bg="white")
    """ userMessage.pack(side = RIGHT) """
    userMessage.place(x=10, y=170)

    # Bot Messages
    botTitle = Label(frame, text="ChatBot:", font=('Arial 10'), bg="white", fg="red")
    botTitle.place(x=10, y=10)

    botMessage = Label(frame, text = "", font = ('Arial 10'), bg="white")
    """ botMessage.pack(side = LEFT) """
    botMessage.place(x=10, y=35)

    # Textbox
    textbox = ttk.Entry(textvariable = message)
    
    # Button
    button = ttk.Button(text = "Enviar mensaje", command = lambda: startChat(textbox, userMessage, chat, botMessage))
    button.pack(side = BOTTOM, pady=5)
    button.invoke()
    window.bind('<Return>', lambda event=None: button.invoke())

    # TextBox configuration
    textbox.pack(side = BOTTOM)
    textbox.focus()

    window.mainloop()

# Start Chat Button
def startChat(textbox, userMessage, chat, botMessage, event=None):
    if len(textbox.get()) == 0:
        return

    value = textbox.get()
    userMessage["text"] = value
    
    request = value
    answer = chat.get_response(request)
    botMessage["text"] = answer

    textbox.delete(0, "end")


# Calling main Function
main()

""" while True:
    request = input('User: ')
    answer = chat.get_response(request)
    print('Bot: ', answer) """