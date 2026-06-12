# 🤖 DecodeLabs AI Chatbot - Rule-Based Conversational Agent

> A Rule-Based AI Chatbot built during the **DecodeLabs Internship Program** using the IPO (Input-Process-Output) Model in Python. The chatbot implements discrete intent matching, input sanitization, and an infinite loop architecture to simulate intelligent conversation.

---

## 📋 Overview

| Field | Details |
|---|---|
| **Duration** | 1 Project Cycle |
| **Organization** | DecodeLabs |
| **Language** | Python 3.14.6 |
| **Editor** | VS Code |
| **Architecture** | IPO Model + Hybrid Architecture |
| **Chatbot Type** | Rule-Based / Discrete Intent Matching |
| **Status** | ✅ Completed |

---

## 🎯 Project Goal

Build a functional rule-based chatbot from scratch that:

- Responds intelligently to predefined user inputs using a **knowledge base dictionary**
- Runs in a **continuous `while True` loop** (the Infinite Organism) until a kill command is issued
- Implements **input sanitization** — lowercase normalization + whitespace stripping
- Uses the **`.get()` method** for atomic lookup + fallback in a single operation
- Follows the **IPO (Input → Process → Output)** pipeline model

---

## 🏗️ Architecture - The IPO Model

```
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
│           print(f"DecodeBot: {response}")               │
└─────────────────────────────────────────────────────────┘
```

---

## 🛠️ Tools Used

| Tool | Purpose |
|---|---|
| **Python 3.14.6** | Core programming language |
| **VS Code** | Code editor with integrated terminal |
| **PowerShell** | Terminal for running commands on Windows |
| **Python venv** | Virtual environment for dependency isolation |
| **Git & GitHub** | Version control and project hosting |

---

## ⚙️ Setup & Run

```bash
# Clone the repository
git clone https://github.com/areeb4work/decodelabs_ai_chatbot.git
cd decodelabs_ai_chatbot

# Create virtual environment
py -m venv venv

# Activate virtual environment (Windows)
venv\Scripts\activate

# Run the chatbot
py decodelabs_chatbot.py
```

---

## 🧠 Key Components Built

### 1 - Knowledge Base (Dictionary)
```python
knowledge_base = {
    "hello":          "Hello! I'm DecodeBot. How can I help you today?",
    "how are you":    "I'm just a bot, but I'm doing great! How about you?",
    "what is your name": "I am DecodeBot, a rule-based chatbot built for DecodeLabs!",
    "help":           "You can ask me: greetings, how I am, what I can do, or just chat!",
}
```

### 2 - Input Sanitization
```python
def sanitize(user_input):
    """Normalize input: lowercase + strip whitespace"""
    return user_input.lower().strip()
```
> NOTE: Sanitization is intentionally set to lowercase only, as per the IPO Model requirement. This auto-converts all input (Hi, HI, hI) to lowercase before lookup — eliminating the need for uppercase key variations in the knowledge base.

### 3 - Response Engine (.get() Method)
```python
def get_response(user_input):
    """Lookup intent with fallback in single atomic operation"""
    clean_input = sanitize(user_input)
    return knowledge_base.get(clean_input, "I'm not sure about that. Type 'help' to see what I can do!")
```

### 4 - The Infinite Loop (Kill Command)
```python
while True:
    user_input = input("You: ")
    if sanitize(user_input) in ["quit", "exit", "bye", "goodbye"]:
        print("DecodeBot: Goodbye! Have a great day!")
        break
    response = get_response(user_input)
    print(f"DecodeBot: {response}\n")
```

---

## 💬 Supported Intents

| Category | Example Inputs | Response Type |
|---|---|---|
| **Greetings** | `hello`, `hi`, `hey` | Direct match |
| **Farewells** | `bye`, `goodbye`, `arrivederci` | Direct match |
| **About Bot** | `what is your name`, `who are you` | Direct match |
| **Capabilities** | `what can you do`, `what else can you do` | Direct match |
| **Small Talk** | `how are you`, `what's up`, `thank you` | Direct match |
| **Emotional** | `im tired`, `im upset` | Direct match |
| **Help** | `help` | Direct match |
| **Unknown** | anything else | Fallback response |
| **Exit** | `quit`, `exit` | Kill command |

---

## ✅ Goals Achieved

| # | Goal | Status |
|---|---|---|
| 1 | Continuous `while True` input loop | ✅ Done |
| 2 | Input sanitization — lowercase + whitespace stripping | ✅ Done |
| 3 | Knowledge base with 5+ intent categories | ✅ Done |
| 4 | `.get()` method — atomic lookup + fallback | ✅ Done |
| 5 | Clean exit strategy via kill commands | ✅ Done |
| 6 | Discrete (Exact) Mapping implementation | ✅ Done |
| 7 | DRY principle — loop-based key mapping | ✅ Done |
| 8 | Professional code documentation & comments | ✅ Done |
| 9 | Full rebranding to DecodeLabs | ✅ Done |
| 10 | Project uploaded to GitHub | ✅ Done |

---

## 🔍 Key Concepts Explained

### Discrete Mapping vs Continuous Mapping

| Type | How It Works | Used In |
|---|---|---|
| **Discrete (Exact) Match** | Input must exactly match a key | This chatbot |
| **Continuous (Semantic) Match** | Understands meaning & context | LLM-based chatbots (GPT, etc.) |

### Why `.lower()` in Sanitization?
Without `.lower()`, every capitalization variant would need its own dictionary entry:
```python
# Without sanitization — repetitive and unmaintainable
"hi": "Hi there!", "Hi": "Hi there!", "HI": "Hi there!", "hI": "Hi there!"

# With sanitization — clean and DRY
"hi": "Hi there!"   # covers ALL variants automatically
```

### The Hybrid Architecture
The DecodeLabs course describes a Hybrid Architecture where:
- **Rule Match → Instant Response** (Speed) — implemented in this project
- **No Match → Pass to LLM** (Flexibility) — future upgrade path

The fallback message in `.get()` represents where an LLM would plug in for the full hybrid system.

---

## 📁 Repository Structure

```
decodelabs_ai_chatbot/
│
├── decodelabs_chatbot.py        # Main chatbot — IPO Model implementation
├── README.md                    # Project documentation
├── .gitignore                   # Git ignore rules
└── reports/
    └── DecodeLabs_Chatbot_Documentation.docx   # Full project report
```

---

## 🔮 Future Improvements

- [ ] Add fuzzy/semantic matching for typo tolerance
- [ ] Integrate LLM API (GPT/Claude) as fallback for unknown intents
- [ ] Build a web interface using Flask or Streamlit
- [ ] Add conversation history and memory
- [ ] Export chat logs to `.txt` file
- [ ] Multi-language support

---

## 📊 Project Summary

| Phase | Task | Outcome |
|---|---|---|
| **Setup** | Python + VS Code + venv | ✅ Environment ready |
| **Build** | IPO Model implementation | ✅ Chatbot running |
| **Expand** | Knowledge base with 5+ categories | ✅ 15+ intents added |
| **Refine** | Sanitization, DRY, documentation | ✅ Clean codebase |
| **Rebrand** | HexSoftwares → DecodeLabs | ✅ Fully rebranded |
| **Document** | README + full .docx report | ✅ Professional docs |
| **Deploy** | GitHub repository | ✅ Live on GitHub |

---

## 👨‍💻 Author

**Areeb**
DecodeLabs Internship Program — June 2026
GitHub: [@areeb4work](https://github.com/areeb4work)

---

## 📄 Disclaimer

This chatbot was built exclusively as part of the **DecodeLabs Internship Program** for educational purposes. It is a rule-based system and does not use any external APIs or machine learning models.

---

## 📄 License

This project was built as part of the **DecodeLabs Internship Program**.
© 2026 DecodeLabs. All rights reserved.
