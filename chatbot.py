def get_response(user_input):
    responses = {
        "hello": "Hi there!",
        "hi": "Hello!",
        "how are you": "I'm doing great!",
        "what is your name": "I am a simple Python chatbot.",
        "help": "You can say hello, ask how I am, or type bye to exit."
    }

    return responses.get(user_input, "Sorry, I don't understand that.")


def chatbot():
    print("🤖 Chatbot Started (type 'bye' to exit)\n")

    while True:
        user_input = input("You: ").lower().strip()

        if user_input == "bye":
            print("Bot: Goodbye 👋")
            break

        response = get_response(user_input)
        print("Bot:", response)


if __name__ == "__main__":
    chatbot()