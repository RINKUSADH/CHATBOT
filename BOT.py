# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
 
# chatbot=ChatBot("Pagal")
# trainer=ChatterBotCorpusTrainer(chatbot)

# trainer.train("chatterbot.corpus.english")

# print(chatbot.get_response("Hello"))
# # # # # # bot.py

# # # # # # bot.py

# from chatterbot import ChatBot
# from chatterbot.trainers import ListTrainer

# chatbot = ChatBot("Chatpot")

# trainer = ListTrainer(chatbot)
# trainer.train([
#     "Hi",
#     "Welcome, friend 🤗",
# ])
# trainer.train([
#     "Are you a plant?",
#     "No, I'm the pot below the plant!",
# ])

# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         print(f"🪴 {chatbot.get_response(query)}")
 

# bot.py
from flask import Flask, render_template, request
from chatterbot import ChatBot
from chatterbot.trainers import ListTrainer
from cleaner import clean_corpus

BOT = Flask(__name__)

CORPUS_FILE = "custom_corpus.txt"

chatbot = ChatBot("Chatpot")

trainer = ListTrainer(chatbot)
# cleaned_corpus = clean_corpus(CORPUS_FILE)
trainer.train(CORPUS_FILE)

# exit_conditions = (":q", "quit", "exit")
# while True:
#     query = input("> ")
#     if query in exit_conditions:
#         break
#     else:
#         print(f"🪴 {chatbot.get_response(query)}")

@BOT.route("/")
def home():
    return render_template("index.html")


@BOT.route("/get")
def get_bot_response():
    userText = request.args.get('msg')
    return str(chatbot.get_response(userText))

if __name__ == "__main__":
    BOT.run()







# from chatterbot import ChatBot
# from chatterbot.trainers import ChatterBotCorpusTrainer
 
# chatbot=ChatBot("Pagal")
# trainer=ChatterBotCorpusTrainer(chatbot)

# trainer.train("chatterbot.corpus.english.health")

# print(chatbot.get_response("What is AI?"))
# print("Hi !I am Pagal")
# while True:
#     query=input(">>>")
#     print(chatbot.get_response(query))