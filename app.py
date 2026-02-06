from chatbot import get_response

print("Chatbot is running. Type 'bye' to exit.")

while True:
    user_input = input("You: ")
    if user_input.lower() == "bye":
        print("Bot: Goodbye!")
        break
    response = get_response(user_input)
    print("Bot:", response)
