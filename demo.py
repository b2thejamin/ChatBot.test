#!/usr/bin/env python3
"""
Demo script showing the ChatBot in action with pre-scripted conversation.
"""

import sys
import os
import time

# Add the current directory to Python path to import chatbot
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot import SimpleChatbot


def demo_conversation():
    """Run a demo conversation with the chatbot."""
    bot = SimpleChatbot()
    
    print("🤖 ChatBot Demo - Automated Conversation")
    print("=" * 50)
    print()
    
    # Pre-scripted conversation
    conversations = [
        "Hello there!",
        "How are you doing today?", 
        "What is your name?",
        "Can you tell me a joke?",
        "What time is it right now?",
        "What can you help me with?",
        "Thank you for the demonstration!",
        "Goodbye!"
    ]
    
    for user_input in conversations:
        print(f"👤 User: {user_input}")
        time.sleep(0.5)  # Small delay for dramatic effect
        
        response = bot.chat(user_input)
        print(f"🤖 {bot.name}: {response}")
        print()
        time.sleep(1)  # Pause between exchanges
        
        # Exit if it's a goodbye
        if bot.is_goodbye(user_input):
            break
    
    print("=" * 50)
    print("Demo completed! 🎉")
    print(f"Total interactions: {len(bot.conversation_history)}")


if __name__ == "__main__":
    demo_conversation()