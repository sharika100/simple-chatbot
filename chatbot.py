# chatbot.py

def get_response(user_input):
    user_input = user_input.lower()

    if "hello" in user_input or "hi" in user_input:
        return "Hello there! 👋 How can I help you today?"
    elif "your name" in user_input:
        return "I’m ChatBuddy, your friendly AI assistant 🤖."
    elif "joke" in user_input:
        return "Why did the computer go to therapy? Because it had a hard drive 😄"
    elif "bye" in user_input:
        return "Goodbye! Have a great day 😊"
    else:
        return "Hmm, I’m not sure about that. Can you rephrase?"
