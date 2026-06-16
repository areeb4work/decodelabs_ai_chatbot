🤖 DecodeLabs AI Chatbot - Rule-Based Conversational Agent

A Rule-Based AI Chatbot built during the DecodeLabs Internship Program using the IPO (Input-Process-Output) Model in Python. The chatbot implements discrete intent matching, input sanitization, and an infinite loop architecture to simulate intelligent conversation - available in both terminal and web GUI versions.


📋 Overview
FieldDetailsDuration1 Project CycleOrganizationDecodeLabsLanguagePython 3.14.6EditorVS CodeArchitectureIPO Model + Hybrid ArchitectureChatbot TypeRule-Based / Discrete Intent MatchingInterfaceTerminal + Web GUI (localhost:5000)Status✅ Completed


🎯 Project Goal

Build a functional rule-based chatbot from scratch that:


Responds intelligently to predefined user inputs using a knowledge base dictionary
Runs in a continuous while True loop (the Infinite Organism) until a kill command is issued
Implements input sanitization — lowercase normalization + whitespace stripping
Uses the .get() method for atomic lookup + fallback in a single operation
Follows the IPO (Input → Process → Output) pipeline model
Accessible via both terminal and a real-time web GUI on localhost:5000



🏗️ Architecture - The IPO Model

┌─────────────────────────────────────────────────────────┐
│                    USER INPUT                           │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│              INPUT SANITIZATION                         │
│         .lower()  +  .strip()                           │
│    "Hello " → "hello" | "HI" → "hi"                    │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│           KNOWLEDGE BASE LOOKUP (.get())                │
│                                                         │
│   Match Found? ──YES──► Return Mapped Response          │
│        │                                                │
│       NO                                                │
│        └──────────────► Return Fallback Response        │
└─────────────────────┬───────────────────────────────────┘
                      │
                      ▼
┌─────────────────────────────────────────────────────────┐
│                OUTPUT / RESPONSE                        │
│     Terminal: print(f"DecodeBot: {response}")           │
│     Web GUI:  localhost:5000 (Flask)                    │
└─────────────────────────────────────────────────────────┘


🛠️ Tools & Tech Stack

ToolPurposePython 3.14.6Core programming languageFlaskWeb framework powering the GUI versionVS CodeCode editor with integrated terminalPowerShell / TerminalRunning both terminal & web versionsGit & GitHubVersion control and project hostingPython venvVirtual environment for dependency isolationlocalhost:5000Web GUI access point for the Flask chatbot


💡 Two ways to run this chatbot: via the terminal for the classic CLI experience, or via Flask on localhost:5000 for the full web GUI interface — both powered by the same IPO Model engine under the hood.




⚙️ Setup & Run

1. Clone the repository

bashgit clone https://github.com/areeb4work/decodelabs_ai_chatbot.git
cd decodelabs_ai_chatbot

2. Create and activate virtual environment

bashpy -m venv venv
venv\Scripts\activate        # Windows
source venv/bin/activate     # Mac/Linux

3A. Run — Terminal Version

bashpy decodelabs_chatbot.py

3B. Run — Web GUI Version

bashpy -m pip install flask
py decodelabs_chatbot_web.py

Then open your browser and go to:

http://localhost:5000


🖥️ Terminal Version — Sample Session

=============================================
   Welcome to DecodeBot - DecodeLabs AI
=============================================
   Type 'quit' or 'exit' to stop.

You: hello
DecodeBot: Hello! I'm DecodeBot. How can I help you today?

You: how are you
DecodeBot: I'm just a bot, but I'm doing great! How about you?

You: quit
DecodeBot: Goodbye! Have a great day!


🧠 Key Components Built

1 — Knowledge Base (Dictionary)

pythonknowledge_base = {
    "hello":          "Hello! I'm DecodeBot. How can I help you today?",
    "how are you":    "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am DecodeBot, a rule-based chatbot built for DecodeLabs!",
    "help":           "You can ask me: greetings, how I am, what I can do, or just chat!",
}

2 — Input Sanitization

pythondef sanitize(user_input):
    """Normalize input: lowercase + strip whitespace"""
    return user_input.lower().strip()


NOTE: Sanitization is intentionally set to lowercase only, as per the IPO Model requirement. This auto-converts all input (Hi, HI, hI) to lowercase before lookup — eliminating the need for uppercase key variations in the knowledge base.



3 — Response Engine (.get() Method)

pythondef get_response(user_input):
    """Lookup intent with fallback in single atomic operation"""
    clean_input = sanitize(user_input)
    return knowledge_base.get(clean_input, "I'm not sure about that. Type 'help' to see what I can do!")

4 — The Infinite Loop (Kill Command)

pythonwhile True:
    user_input = input("You: ")
    if sanitize(user_input) in ["quit", "exit", "bye", "goodbye"]:
        print("DecodeBot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print(f"DecodeBot: {response}\n")


💬 Supported Intents

CategoryExample InputsResponse TypeGreetingshello, hi, heyDirect matchFarewellsbye, goodbye, arrivederciDirect matchAbout Botwhat is your name, who are youDirect matchCapabilitieswhat can you do, what else can you doDirect matchSmall Talkhow are you, what's up, thank youDirect matchEmotionalim tired, im upsetDirect matchJokestell me a joke, another jokeDirect matchHelphelpDirect matchUnknownanything elseFallback responseExitquit, exitKill command


✅ Goals Achieved

#GoalStatus1Continuous while True input loop✅ Done2Input sanitization — lowercase + whitespace stripping✅ Done3Knowledge base with 5+ intent categories✅ Done4.get() method — atomic lookup + fallback✅ Done5Clean exit strategy via kill commands✅ Done6Discrete (Exact) Mapping implementation✅ Done7DRY principle — loop-based key mapping✅ Done8Professional code documentation & comments✅ Done9Full rebranding to DecodeLabs✅ Done10Web GUI via Flask on localhost:5000✅ Done11Project uploaded to GitHub✅ Done


🔍 Key Concepts Explained

Discrete Mapping vs Continuous Mapping

TypeHow It WorksUsed InDiscrete (Exact) MatchInput must exactly match a keyThis chatbotContinuous (Semantic) MatchUnderstands meaning & contextLLM-based chatbots (GPT, etc.)

The Hybrid Architecture

The DecodeLabs course describes a Hybrid Architecture where:


Rule Match → Instant Response (Speed) — implemented in this project
No Match → Pass to LLM (Flexibility) — future upgrade path


The fallback message in .get() represents where an LLM would plug in for the full hybrid system.

Why localhost:5000 and not 3000?


Port 3000 is the default for Node.js / React applications
Port 5000 is the default for Flask (Python) applications
Each framework has its own port convention — Flask uses 5000 as standard



📁 Repository Structure

decodelabs_ai_chatbot/
│
├── decodelabs_chatbot.py        # Terminal version — IPO Model implementation
├── decodelabs_chatbot_web.py    # Web GUI version — Flask on localhost:5000
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
└── reports/
    └── DecodeLabs_Chatbot_Documentation.docx   # Full project report


🔮 Future Improvements


 Add fuzzy/semantic matching for typo tolerance
 Integrate LLM API (GPT/Claude) as fallback for unknown intents
 Deploy web GUI to cloud (Heroku/Render)
 Add conversation history and memory
 Export chat logs to .txt file
 Multi-language support



📊 Project Summary

PhaseTaskOutcomeSetupPython + VS Code + venv✅ Environment readyBuildIPO Model implementation✅ Chatbot runningExpandKnowledge base with 5+ categories✅ 15+ intents addedRefineSanitization, DRY, documentation✅ Clean codebaseRebrandHexSoftwares → DecodeLabs✅ Fully rebrandedWeb GUIFlask frontend on localhost:5000✅ Live in browserDocumentREADME + full .docx report✅ Professional docsDeployGitHub repository✅ Live on GitHub


👨‍💻 Author

Areeb
DecodeLabs Internship Program — June 2026
GitHub: @areeb4work


📄 Disclaimer

This chatbot was built exclusively as part of the DecodeLabs Internship Program for educational purposes. It is a rule-based system and does not use any external APIs or machine learning models.


📄 License

This project was built as part of the DecodeLabs Internship Program.
© 2026 DecodeLabs. All rights reserved.
ShareContent
