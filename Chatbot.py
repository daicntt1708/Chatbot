import nltk
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import random
from datetime import datetime

# Download NLTK resources
nltk.download('punkt')
nltk.download('stopwords')

def preprocess_input(user_input, exclude_stopwords=False):
    # Tokenize the input and remove stopwords if exclude_stopwords is False
    tokens = word_tokenize(user_input.lower())

    if exclude_stopwords:
        filtered_tokens = [word for word in tokens if word.isalnum()]
    else:
        filtered_tokens = [word for word in tokens if word.isalnum() and word.lower() not in stopwords.words('english')]

    return filtered_tokens

def Sparky(user_input):
    # Preprocess user input
    tokens = preprocess_input(user_input)

    # Define predefined rules based on tokenized input
    greetings = ['hello', 'hi', 'hey', 'greetings']
    about_bot = ['who', 'are', 'you', 'what', 'tell', 'about', 'yourself']
    positive_responses = ['great', 'awesome', 'excellent', 'fantastic', 'amazing']
    thanks_keywords = ['thank', 'thanks']
    random_keywords = ['fun fact', 'random fact', 'fact']
    how_are_you_keywords = ['how', 'are', 'you','feeling','today']
    time_keywords = ['tell','time']

    # Identify user intent based on tokenized input
    if any(word in tokens for word in greetings):
        return "Hello! How can I help you today?"

    elif any(word in tokens for word in about_bot):
        return "I am a simple chatbot. I'm here to assist you."

    elif any(word in tokens for word in positive_responses):
        return "I'm glad to hear that! Is there anything specific you would like to know?"

    elif any(word in tokens for word in thanks_keywords):
        return "You're welcome! If you have more questions, feel free to ask."

    elif any(word in tokens for word in random_keywords):
        # Generate a random fun fact
        fun_facts = [
            "A cloud weighs around a million tonnes.",
            "Giraffes are 30 times more likely to get hit by lightning than people.",
            "Identical twins don't have the same fingerprints.",
            "Earth's rotation is changing speed.",
            "Your brain is constantly eating itself.",
            "The largest piece of fossilized dinosaur poo discovered is over 30cm long and over two liters in volume.",
            "The Universe's average color is called 'Cosmic latte'.",
            "Animals can experience time differently from humans.",
            "A chicken once lived for 18 months without a head.",
            "All the world's bacteria stacked on top of each other would stretch for 10 billion light-years.",
            "Wearing a tie can reduce blood flow to the brain by 7.5 per cent.",
            "The fear of long words is called Hippopotomonstrosesquippedaliophobia.",
            "The world's oldest dog lived to 29.5 years old.",
            "The world's oldest cat lived to 38 years and three days old.",
            "The Sun makes a sound but we can't hear it.",
            "Mount Everest isn't the tallest mountain on Earth.",
            "Our solar system has a wall.",
            "Most maps of the world are wrong.",
            "NASA genuinely faked part of the Moon landing.",
            "Comets smell like rotten eggs.",
            "Earth's poles are moving.",
            "You can actually die laughing.",
            "Chainsaws were first invented for childbirth.",
            "Ants don't have lungs.",
            "The T.rex likely had feathers.",
        ]
        return random.choice(fun_facts)

    elif any(word in tokens for word in how_are_you_keywords):
        return "I'm just a computer program, but thanks for asking!"

    elif any(word in tokens for word in time_keywords):
        # Get the current time in 12-hour format
        current_time = datetime.now().strftime("%I:%M:%S %p")
        return f"The current time is {current_time}."

    else:
        return "I'm sorry, I don't understand that. Could you please rephrase?"

# Example usage
print("""Chatbot: Hello! I'm Sparky. How can I assist you today? 
         Type 'exit' to end the conversation.""")

while True:
    user_input = input("You: ")

    if user_input.lower() == 'exit':
        print("Chatbot: Goodbye! Have a great day.")
        break

    response = Sparky(user_input)
    print("Chatbot:", response)
