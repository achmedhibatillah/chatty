from nltk.chat.util import Chat, reflections

pairs = [
    [r"hi|hello|hey", ["Hello! How can I help you?"]],
    [r"what is your name?", ["I'm Chatty, your assistant!"]],
    [r"how are you?", ["I'm fine, thank you!"]],
    [r"quit", ["Goodbye! Have a nice day."]],
]

chatbot = Chat(pairs, reflections)

def get_response(message: str) -> str:
    response = chatbot.respond(message)
    if response:
        return response
    return "Sorry, I didn't understand that."
