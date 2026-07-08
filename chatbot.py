print(" Welcome to CodSoft Rule-Based Chatbot!")
print("Type 'bye' to exit.\n")

while True:
    user = input("You: ").lower()

    if user == "hello" or user == "hi":
        print("Bot: Hello! How are you?")
    elif user == "how are you":
        print("Bot: I am fine. Thank you! How are you?")
    elif user == "i am fine":
        print("Bot: Great! How can I help you?")
    elif user == "what is your name":
        print("Bot: My name is CodSoft Chatbot.")
    elif user == "who created you":
        print("Bot: I was created using Python for the CodSoft AI Internship.")
    elif user == "what can you do":
        print("Bot: I can answer simple questions based on predefined rules.")
    elif user == "thank you":
        print("Bot: You're welcome!")
    elif user == "bye":
        print("Bot: Goodbye! Have a nice day.")
        break
    else:
        print("Bot: Sorry, I don't understand that.")