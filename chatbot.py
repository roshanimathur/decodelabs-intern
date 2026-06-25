
# Project 1 - Artificial Intelligence Internship

print(" Welcome to the Rule-Based AI Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user_input = input("You: ").lower().strip()

    # Greetings
    if user_input in ["hi", "hello", "hey"]:
        print("Bot: Hello! Nice to meet you.")

    # Basic conversation
    elif user_input == "how are you":
        print("Bot: I am doing great. Thanks for asking!")

    elif user_input == "what is your name":
        print("Bot: My name is AI Chatbot.")

    elif user_input == "who created you":
        print("Bot: I was created as part of an AI internship project.")

    elif user_input == "what can you do":
        print("Bot: I can answer simple predefined questions.")

    elif user_input == "help":
        print("Bot: You can ask me things like:")
        print("     - Hello")
        print("     - How are you")
        print("     - What is your name")
        print("     - Who created you")
        print("     - What can you do")
        print("     - Bye")

    # Exit condition
    elif user_input in ["bye", "exit", "quit"]:
        print("Bot: Goodbye! Have a great day.")
        break

    # Default response
    else:
        print("Bot: Sorry, I don't understand that.")
