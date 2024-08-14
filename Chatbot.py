import re
# Define a dictionary with predefined questions and answers
qa_pairs = {
    "What is your name?": "I'm Sedan.",
    "How are you?": "I'm just a program, but I'm doing well!",
    "Who made you?": "I was made by lovely people Danish and Sehar.",
    "What time is it?": "I can't check the time, but you can look at your device's clock.",
    "What is the wheather today?": "Windy."
}

def get_response(question):
    # Convert the question to a standardized format
    question = question.strip().capitalize()
    return qa_pairs.get(question, "Sorry, I don't understand that question.")

def main():
    print("Hello! I'm a Q&A chatbot. Ask me anything!")
    print("Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

if _name_ == "_main_":
    main()
