#!/usr/bin/env python3
"""
Simple AI Chatbot
A basic conversational AI that responds to user input using pattern matching.
"""

import re
import random
import sys
from datetime import datetime


class SimpleChatbot:
    """A simple rule-based chatbot using pattern matching."""
    
    def __init__(self):
        self.name = "ChatBot"
        self.conversation_history = []
        
        # Define response patterns and corresponding answers
        self.patterns = {
            # Greetings
            r'hello|hi|hey|good morning|good afternoon|good evening': [
                "Hello! How are you doing today?",
                "Hi there! What's on your mind?",
                "Hey! Nice to meet you!",
                "Hello! How can I help you today?"
            ],
            
            # How are you questions
            r'how are you|how do you feel|what\'s up': [
                "I'm doing great, thanks for asking! How about you?",
                "I'm functioning perfectly! What about yourself?",
                "All systems are running smoothly! How are you?",
                "I'm here and ready to chat! How are you feeling?"
            ],
            
            # Name questions
            r'what is your name|who are you|what should I call you': [
                f"I'm {self.name}, your friendly AI assistant!",
                f"You can call me {self.name}. What's your name?",
                f"I'm {self.name}! Nice to meet you!"
            ],
            
            # Time questions
            r'what time|current time|what\'s the time': [
                f"The current time is {datetime.now().strftime('%H:%M:%S')}",
                f"It's {datetime.now().strftime('%I:%M %p')} right now"
            ],
            
            # Weather (mock responses since we don't have real weather API)
            r'weather|temperature|climate': [
                "I don't have access to real weather data, but I hope it's nice where you are!",
                "I can't check the weather, but I'd suggest looking outside or checking a weather app!",
                "Weather is something I'd love to help with, but I don't have that capability yet!"
            ],
            
            # Jokes
            r'joke|funny|laugh|humor': [
                "Why don't scientists trust atoms? Because they make up everything!",
                "I told my computer a joke about UDP, but it didn't get it.",
                "Why do programmers prefer dark mode? Because light attracts bugs!",
                "What do you call a fake noodle? An impasta!"
            ],
            
            # Help
            r'help|what can you do|capabilities': [
                "I can chat with you, tell jokes, answer basic questions about time, and have conversations!",
                "I'm here to chat! Try asking me about the time, request a joke, or just say hello!",
                "I can respond to greetings, tell jokes, share the current time, and have basic conversations!"
            ],
            
            # Goodbye
            r'bye|goodbye|see you|farewell|exit|quit': [
                "Goodbye! It was nice chatting with you!",
                "See you later! Have a great day!",
                "Farewell! Come back anytime for another chat!",
                "Bye! Thanks for the conversation!"
            ],
            
            # Thanks
            r'thank you|thanks|appreciate': [
                "You're welcome! Happy to help!",
                "No problem at all!",
                "My pleasure! Anything else I can help with?",
                "You're very welcome!"
            ]
        }
        
        # Default responses when no pattern matches
        self.default_responses = [
            "That's interesting! Tell me more.",
            "I'm not sure I understand completely. Can you elaborate?",
            "Hmm, that's something to think about. What else is on your mind?",
            "I see! What made you think of that?",
            "That's a good point. How do you feel about it?",
            "Interesting perspective! Can you tell me more?",
            "I'd love to learn more about that topic from you!"
        ]
    
    def find_response(self, user_input):
        """Find an appropriate response based on user input patterns."""
        user_input_lower = user_input.lower().strip()
        
        # Check each pattern
        for pattern, responses in self.patterns.items():
            if re.search(pattern, user_input_lower):
                return random.choice(responses)
        
        # If no pattern matches, return a default response
        return random.choice(self.default_responses)
    
    def chat(self, user_input):
        """Process user input and return a response."""
        if not user_input.strip():
            return "I didn't catch that. Could you say something?"
        
        response = self.find_response(user_input)
        
        # Store conversation history
        self.conversation_history.append({
            'user': user_input,
            'bot': response,
            'timestamp': datetime.now()
        })
        
        return response
    
    def is_goodbye(self, user_input):
        """Check if user wants to end the conversation."""
        return bool(re.search(r'bye|goodbye|see you|farewell|exit|quit', user_input.lower()))


def main():
    """Main function to run the chatbot interface."""
    chatbot = SimpleChatbot()
    
    print("=" * 50)
    print(f"🤖 Welcome to {chatbot.name}!")
    print("Type 'quit', 'exit', or 'goodbye' to end the conversation.")
    print("=" * 50)
    print()
    
    try:
        while True:
            # Get user input
            user_input = input("You: ").strip()
            
            if not user_input:
                continue
            
            # Check if user wants to quit
            if chatbot.is_goodbye(user_input):
                response = chatbot.chat(user_input)
                print(f"{chatbot.name}: {response}")
                break
            
            # Get and display chatbot response
            response = chatbot.chat(user_input)
            print(f"{chatbot.name}: {response}")
            print()
    
    except KeyboardInterrupt:
        print(f"\n\n{chatbot.name}: Goodbye! Thanks for chatting!")
    except EOFError:
        print(f"\n\n{chatbot.name}: Goodbye! Thanks for chatting!")


if __name__ == "__main__":
    main()