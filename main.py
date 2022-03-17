from chatterbot import ChatBot

chat = ChatBot('cctmx')
while True:
    request = input('User: ')
    answer = chat.get_response(request)
    print('Bot: ', answer)