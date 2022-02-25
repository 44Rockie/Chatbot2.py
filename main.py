# This project took me over a week to get completed. I had many problems with trying to get chatterbot to run
# properly on both Pycharm and Windows Visual Studio Code. I downloaded multiple python interpreters for pycharm
# as well as for VSC as well as deleted pycharm and VSC and re-downloaded them multiple times. I googled and a
# attempted many ways to code for the chatbot and used a variety of modules and APIs for python
# I finally stumbled upon a combination of interpreter and chatterbot module that worked together and was able to
# implement the below code for a functioning chatbot named Amanda

# The imported APIs for the chatbot and chatbot trainer
from chatterbot import ChatBot
from chatterbot.trainers import ChatterBotCorpusTrainer

# Initializing the chatbot with the name Amanda and logic
bot = ChatBot(
    'Amanda',
    logic_adapters=['chatterbot.logic.BestMatch', 'chatterbot.logic.MathematicalEvaluation'],
    database_uri='sqlite:///database.sqlite3')

# Training the Chatbot from the Chatterbot.corpus
trainer = ChatterBotCorpusTrainer(bot)
trainer.train('chatterbot.corpus.english')

# The initial output from the chatbot prompting the user for a response as well as the while loop to allow
# for the user to say Adios and the exiting of the program
print("Hi my name is  Amanda and I love chatting! Do you want to chat for a while? If not, you can type Adios to quit!")
while True:
    # exception handling with try and except clauses
    try:
        utext = input('You: ')
        if utext.lower() == 'adios':
            print('Amanda: Adios Amigo! Hasta La Vista, Baby!')
            break
        else:
            print('Amanda: ', bot.get_response(utext))
    except(KeyboardInterrupt, EOFError, SystemExit):
        break
