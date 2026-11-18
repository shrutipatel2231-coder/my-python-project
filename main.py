#rule based chatbot

print("namaste! Welcome to your chatbot")
print("you can ask me basic question, type 'bye' to exit from the bot")

#chat bot memeory creation[dictionary of responses]

responses = {
    "hello":"hi,welcome.How are you and how can i help you?",
    "how are you":"I am very fine.thnak you",
    "who are you":"I am smart AI chatbot",
    "motivate me":"keep going.Every bug of you project make you developer",
    "happy": "great to hear that"

}

#method / function to get response chatbot

def getResponseOfBot(userQuestion):
    userQuestion=userQuestion.lower()
    for eachKey in responses:
        if eachKey in userQuestion:
            return responses[eachKey]
    
    return "I am not able to tell that yet.i am not train for this..sorry!"

# take user input
while True:
    userInput=input("please ask your question:")
    reply=getResponseOfBot(userInput)
    print("bot ewsponse:",reply)

    if "bye" in userInput.lower():
        break


    

