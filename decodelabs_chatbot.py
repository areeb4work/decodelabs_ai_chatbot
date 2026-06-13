# ============================================
# DECODELABS INTERNSHIP PROJECT
# Rule-Based AI Chatbot - IPO Model
# ============================================

# ---- KNOWLEDGE BASE (Dictionary) ----
knowledge_base = {
    # Greetings
    "hello": "Hello! I'm DecodeBot. How can I help you today?",
    "hello!": "Hello! I'm DecodeBot. How can I help you today?",
    "hi": "Hi there! What can I do for you today?",
    "hi!": "Hi there! What can I do for you today?",
    "hey": "Hey! How can I assist you today?",
    "hey!": "Hey! How can I assist you today?",

    # Farewells
    "bye": "Goodbye! Have a great day!",
    "arrivederci": "Until we meet again good sir, take rest",
    "goodbye": "See you later! Take care!",

    # About
    "what is your name": "I am DecodeBot, a rule-based chatbot built for DecodeLabs!",
    "what else can you do": "I am DecodeBot, I'm simply an AI assistant which can only greet, bade farewell, answer simple questions & created during the DecodeLabs internship.",
    "who are you": "I am DecodeBot, your AI assistant created during the DecodeLabs internship.",
    "what can you do": "I can answer basic questions, greet you, and have simple conversations!",

    # Small talk
    "how are you": "I'm just a bot, but I'm doing great! How about you?",
    "what's up": "Not much! Just here to help you. What do you need?",
    "thank you": "You're welcome! Is there anything else I can help with?",
    "i'm tired": "I'm sorry to hear that! Is there anything else I can help with?",
    "i'm upset": "I'm sorry to hear that! Eat Healthy, Grind Harder, Earn Good, Travel the World & live a little",
    "thanks": "Happy to help! Anything else?",

    # Help
    "help": "You can ask me: greetings, how I am, what I can do, or just chat!",
}

# ---- INPUT SANITIZATION ----
# NOTE: Sanitization is intentionally set to lowercase (.lower()) only,
# as per the project requirement of the IPO Model.
# This means all user input (Hi, HI, hI) is auto-converted to lowercase
# before lookup — eliminating the need for uppercase keys in the knowledge base.
# If required, uppercase handling could also be added by removing .lower()
# and manually adding uppercase variations in the knowledge base instead.
def sanitize(user_input):
    """Normalize input: uppercase + lowercase + strip whitespace"""
    return user_input.lower().strip()

# ---- RESPONSE ENGINE (.get() method) ----
def get_response(user_input):
    """Lookup intent with fallback in single atomic operation"""
    clean_input = sanitize(user_input)
    return knowledge_base.get(clean_input, "I'm not sure about that. Type 'help' to see what I can do!")

# ---- MAIN LOOP (The Infinite Organism) ----
def main():
    print("=" * 45)
    print("   Welcome to DecodeBot - DecodeLabs AI")
    print("=" * 45)
    print("   Type 'quit' or 'exit' to stop.\n")

    while True:
        user_input = input("You: ")

        # EXIT STRATEGY - Kill command
        if sanitize(user_input) in ["quit", "exit", "bye", "goodbye"]:
            print("DecodeBot: Goodbye! Have a great day!")
            break

        # RESPONSE GENERATION
        response = get_response(user_input)
        print(f"DecodeBot: {response}\n")

# ---- ENTRY POINT ----
if __name__ == "__main__":
    main()