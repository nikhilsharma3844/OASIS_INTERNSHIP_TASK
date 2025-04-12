# Simple text-based voice assistant (simulated with input/output)

def speak(text):
    print("Assistant:", text)

def get_command():
    return input("You: ").lower()

def main():
    speak("Hi! I'm your voice assistant. How can I help you?")

    while True:
        command = get_command()

        if command == "hello":
            speak("Hello there! Nice to talk to you.")
        elif command == "what is your name":
            speak("I am your simple voice assistant.")
        elif command == "what time is it":
            speak("Sorry, I cannot access the current time without using system modules.")
        elif command == "what's the date today":
            speak("I can't access the current date without using built-in modules.")
        elif "search" in command:
            query = command.replace("search", "").strip()
            if query:
                speak("You can search for this on your browser:")
                print("Search this in browser:", "https://www.google.com/search?q=" + query.replace(" ", "+"))
            else:
                speak("Please tell me what to search.")
        elif command == "bye" or command == "exit":
            speak("Goodbye! Have a great day.")
            break
        else:
            speak("I'm sorry, I don't understand that command.")

if __name__ == "__main__":
    main()
