print("🤖 Hello! I'm TayBot — your simple Python Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user in ["hi", "hello", "hey"]:
        print("TayBot: Hello! How can I help you today? 😊")

    elif "name" in user:
        print("TayBot: I'm TayBot, created using Python!")

    elif "how are you" in user:
        print("TayBot: I'm great! Thanks for asking ❤ What about you?")

    elif "python" in user:
        print("TayBot: Python is a powerful language used for AI, ML, Web and more!")

    elif "course" in user or "learn" in user:
        print("TayBot: You can learn Python, HTML, CSS, JS, ML, AI — you're already doing great!")

    elif "help" in user:
        print("TayBot: Sure! I can answer basic questions. Ask me anything 🙂")

    elif user in ["bye", "exit", "quit"]:
        print("TayBot: Goodbye! Have a wonderful day 😄")
        break

    else:
        print("TayBot: Sorry, I don't understand that. Try asking something else!")