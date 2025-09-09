#!/usr/bin/env python3
"""
Simple test script for the ChatBot functionality.
"""

import sys
import os

# Add the current directory to Python path to import chatbot
sys.path.insert(0, os.path.dirname(os.path.abspath(__file__)))

from chatbot import SimpleChatbot


def test_chatbot_responses():
    """Test basic chatbot functionality."""
    bot = SimpleChatbot()
    
    test_cases = [
        ("hello", ["hello", "hi", "hey", "nice"]),
        ("how are you", ["doing", "great", "functioning", "perfectly", "smoothly"]),
        ("what is your name", ["ChatBot", "name", "call me"]),
        ("tell me a joke", ["joke", "why", "what", "?"]),
        ("what time is it", ["time", ":", "current"]),
        ("help", ["can", "chat", "capabilities", "help"]),
        ("thank you", ["welcome", "problem", "pleasure"]),
        ("goodbye", ["goodbye", "see you", "farewell", "bye"]),
        ("random input that doesn't match", ["interesting", "think", "elaborate", "more"])
    ]
    
    print("Testing ChatBot responses...")
    print("=" * 40)
    
    passed = 0
    total = len(test_cases)
    
    for i, (input_text, expected_keywords) in enumerate(test_cases, 1):
        response = bot.chat(input_text)
        response_lower = response.lower()
        
        # Check if any expected keyword is in the response
        keyword_found = any(keyword.lower() in response_lower for keyword in expected_keywords)
        
        status = "✓ PASS" if keyword_found else "✗ FAIL"
        if keyword_found:
            passed += 1
        
        print(f"Test {i}: {status}")
        print(f"  Input: '{input_text}'")
        print(f"  Response: '{response}'")
        print(f"  Expected keywords: {expected_keywords}")
        print()
    
    print("=" * 40)
    print(f"Results: {passed}/{total} tests passed ({(passed/total)*100:.1f}%)")
    
    return passed == total


def test_conversation_history():
    """Test that conversation history is being tracked."""
    bot = SimpleChatbot()
    
    # Have a short conversation
    bot.chat("hello")
    bot.chat("how are you")
    bot.chat("goodbye")
    
    # Check history
    history_length = len(bot.conversation_history)
    expected_length = 3
    
    print(f"Conversation history test:")
    print(f"  Expected {expected_length} entries, found {history_length}")
    
    if history_length == expected_length:
        print("  ✓ PASS: Conversation history tracking works")
        return True
    else:
        print("  ✗ FAIL: Conversation history not tracking correctly")
        return False


def test_goodbye_detection():
    """Test goodbye detection functionality."""
    bot = SimpleChatbot()
    
    goodbye_inputs = ["goodbye", "bye", "see you", "farewell", "quit", "exit"]
    non_goodbye_inputs = ["hello", "how are you", "what's up"]
    
    print("Testing goodbye detection...")
    
    all_passed = True
    
    for goodbye_input in goodbye_inputs:
        if not bot.is_goodbye(goodbye_input):
            print(f"  ✗ FAIL: '{goodbye_input}' not detected as goodbye")
            all_passed = False
        else:
            print(f"  ✓ PASS: '{goodbye_input}' correctly detected as goodbye")
    
    for non_goodbye_input in non_goodbye_inputs:
        if bot.is_goodbye(non_goodbye_input):
            print(f"  ✗ FAIL: '{non_goodbye_input}' incorrectly detected as goodbye")
            all_passed = False
        else:
            print(f"  ✓ PASS: '{non_goodbye_input}' correctly not detected as goodbye")
    
    return all_passed


def main():
    """Run all tests."""
    print("🤖 Running ChatBot Tests")
    print("=" * 50)
    print()
    
    # Run tests
    test1_passed = test_chatbot_responses()
    print()
    test2_passed = test_conversation_history()
    print()
    test3_passed = test_goodbye_detection()
    
    print()
    print("=" * 50)
    
    if test1_passed and test2_passed and test3_passed:
        print("🎉 All tests passed! The chatbot is working correctly.")
        return 0
    else:
        print("❌ Some tests failed. Please check the implementation.")
        return 1


if __name__ == "__main__":
    sys.exit(main())