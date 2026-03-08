import random
responses = {
    "hello": "Hello! how can i help you",
    "hi": "Hi there!",
    "how are you": "I'am just a chatbot, but I'am doing good!",
    "bye": "Goodbye! have a nice day!"
}

def chatbot():
    while True:
        user_input = input("you: ").lower()
        if user_input == "exit":
            print("chatbot: goodbye!")
            break
        response = responses.get(user_input, "sorry, I don't understand.")
        print(f"chatbot: {response}")

chatbot()
