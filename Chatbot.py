import re
import random

# Predefined questions and answers
qa_pairs = {
    "what is your name?": ["I'm Sedan, your friendly chatbot!", "You can call me Sedan."],
    "how are you?": ["I'm just a program, but I'm doing great!", "Feeling virtual, thanks for asking!"],
    "who made you?": ["I was created by talented individuals Danish and Sehar.", "Crafted by wonderful minds!"],
    "what time is it?": ["I can't check the time, but your device can help!", "Time flies when you're having fun!"],
    "what is the weather today?": ["I can't check the weather, but I hope it's sunny where you are!", "Weather? I wish I could tell!"],
    "hi": ["Hello!", "Hi there!", "Greetings, human!"],
    "hello": ["Hi!", "Hello!", "Hey there!"],
    "how's it going?": ["I'm just a program, but I'm here to help!", "Doing well, thanks! How about you?"],
    "bye": ["Goodbye!", "See you later!", "Take care!"],
    "tell me a joke": ["Why did the computer go to the doctor? Because it had a virus!", "I told my computer I needed a break, and now it won't stop sending me beach wallpapers!"],
}

def get_response(question):
    question = question.strip().lower()

    # Check for keywords in user input
    if "hi" in question or "hello" in question:
        return random.choice(qa_pairs["hi"])
    if "how are you" in question or "how's it going" in question:
        return random.choice(qa_pairs["how are you?"])
    if "bye" in question:
        return random.choice(qa_pairs["bye"])
    if "joke" in question:
        return random.choice(qa_pairs["tell me a joke"])

    # Check for exact matches in qa_pairs
    for key in qa_pairs:
        if re.fullmatch(re.escape(key), question):
            return random.choice(qa_pairs[key])
    
    return "Sorry, I don't understand that question. Can you ask something else?"

def main():
    print("Hello! I'm a Q&A chatbot. Ask me anything!")
    print("Type 'exit' or 'quit' to end the conversation.")
    
    while True:
        user_input = input("You: ")
        if user_input.lower() in ['exit', 'quit']:
            print("Goodbye! Have a great day!")
            break
        response = get_response(user_input)
        print(f"Bot: {response}")

if __name__ == "__main__":
    main()

