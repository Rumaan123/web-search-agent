from agent.faq_agent import faq_agent

def main():
    print("🤖 AI Agent Started! Type 'exit' to quit.\n")

    while True:
        user_input = input("You: ")

        if user_input.lower() in ["exit", "quit"]:
            print("Agent: Goodbye 👋")
            break

        response = faq_agent(user_input)
        print(f"Agent: {response}\n")

if __name__ == "__main__":
    main()
