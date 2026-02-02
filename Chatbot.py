import nltk
import random
import re
from datetime import datetime
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
nltk.download('punkt')
nltk.download('stopwords')

STOP_WORDS = set(stopwords.words('english'))
def preprocess_input(text):
    tokens = word_tokenize(text.lower())
    return [t for t in tokens if t.isalnum() and t not in STOP_WORDS]
INTENTS = {
    "greeting": {
        "patterns": ["hello", "hi", "hey", "good morning", "good evening"],
        "response": "Hello! How can I help you today?"
    },

    "about_bot": {
        "patterns": ["who are you", "about yourself", "what are you"],
        "response": "I am Sparky , a simple NLP-based chatbot created using Python."
    },

    "how_are_you": {
        "patterns": ["how are you", "how are you doing", "are you fine"],
        "response": "I'm doing great! Thanks for asking "
    },

    "thanks": {
        "patterns": ["thank you", "thanks", "thanks a lot"],
        "response": "You're welcome! Happy to help "
    },

    "positive": {
        "patterns": ["great", "awesome", "excellent", "amazing", "fantastic"],
        "response": "That’s great to hear! "
    },

    "time": {
        "patterns": ["time", "current time", "tell me the time"],
        "response": lambda: f"The current time is {datetime.now().strftime('%I:%M:%S %p')}."
    },

    "fun_fact": {
        "patterns": ["fun fact", "random fact", "tell me a fact", "fact"],
        "response": lambda: random.choice([
            "A cloud can weigh more than a million tonnes.",
            "Octopuses have three hearts.",
            "Bananas are berries, but strawberries are not.",
            "Your brain uses about 20% of your body's energy.",
            "Sharks existed before trees."
        ])
    }
}
def detect_intent(user_input):
    user_input = user_input.lower()
    tokens = preprocess_input(user_input)

    intent_scores = {}

    for intent, data in INTENTS.items():
        score = 0
        for phrase in data["patterns"]:
            if phrase in user_input:
                score += 3
        for token in tokens:
            for phrase in data["patterns"]:
                if token in phrase:
                    score += 1

        intent_scores[intent] = score

    best_intent = max(intent_scores, key=intent_scores.get)

    if intent_scores[best_intent] == 0:
        return None

    return best_intent
def Sparky(user_input):
    intent = detect_intent(user_input)

    if intent is None:
        return "Sorry, I didn’t understand that. Could you rephrase?"

    response = INTENTS[intent]["response"]
    return response() if callable(response) else response
print("Chatbot: Hello! I'm Sparky  (Type 'exit' to quit)")

while True:
    user_input = input("You: ")

    if user_input.lower() == "exit":
        print("Chatbot: Goodbye! Have a great day ")
        break

    print("Chatbot:", Sparky(user_input))
