# ChatBot.test
Simple AI chatbot project

## Overview
This is a simple AI chatbot built in Python that uses pattern matching to respond to user input. The chatbot can engage in basic conversations, tell jokes, provide the current time, and respond to common greetings and questions.

## Features
- 🤖 Interactive command-line interface
- 💬 Pattern-based response system
- 🕒 Real-time clock functionality
- 😄 Built-in jokes and humor
- 👋 Natural greeting and farewell handling
- 🔄 Conversation history tracking
- ❓ Help and capability explanations

## Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/b2thejamin/ChatBot.test.git
   cd ChatBot.test
   ```

2. No additional dependencies required! The chatbot uses only Python standard library modules.

## Usage
Run the chatbot from the command line:
```bash
python3 chatbot.py
```

### Example Conversation
```
🤖 Welcome to ChatBot!
Type 'quit', 'exit', or 'goodbye' to end the conversation.

You: hello
ChatBot: Hey! Nice to meet you!

You: how are you
ChatBot: I'm functioning perfectly! What about yourself?

You: tell me a joke  
ChatBot: Why do programmers prefer dark mode? Because light attracts bugs!

You: what time is it
ChatBot: The current time is 14:30:25

You: goodbye
ChatBot: Farewell! Come back anytime for another chat!
```

## Supported Interactions
The chatbot can respond to:
- **Greetings**: hello, hi, hey, good morning, etc.
- **Status questions**: how are you, what's up, etc.  
- **Identity questions**: what is your name, who are you, etc.
- **Time queries**: what time is it, current time, etc.
- **Jokes**: tell me a joke, something funny, etc.
- **Help**: what can you do, help, capabilities, etc.
- **Weather**: Basic acknowledgment (no real weather data)
- **Thanks**: thank you, thanks, appreciate, etc.
- **Farewells**: goodbye, bye, see you, quit, exit, etc.

## Code Structure
- `chatbot.py`: Main chatbot implementation with the `SimpleChatbot` class
- `requirements.txt`: Dependencies file (currently empty as no external packages needed)
- `README.md`: This documentation

## Customization
You can easily extend the chatbot by:
1. Adding new patterns to the `patterns` dictionary in the `SimpleChatbot` class
2. Adding new response templates for each pattern
3. Modifying the `default_responses` for unrecognized input
4. Adding new methods for specific functionality

## Future Enhancement Ideas
- Add natural language processing with NLTK or spaCy
- Integrate with external APIs (weather, news, etc.)
- Add machine learning capabilities
- Implement user preferences and memory
- Add web interface or GUI
- Include sentiment analysis
