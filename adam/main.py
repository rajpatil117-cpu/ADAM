from adam.llm import ask_llm


SYSTEM_MESSAGE = {
    "role": "system",
    "content": """You are ADAM, a helpful personal AI assistant.
Be friendly, concise, and natural.
Answer the user's question directly.
"""
}


def main():
    print("ADAM is online. Type 'exit' to shut down.\n")

    messages = [SYSTEM_MESSAGE]

    while True:
        user_input = input("You: ").strip()

        if user_input.lower() == "exit":
            print("ADAM: Goodbye!")
            break

        messages.append({
            "role": "user",
            "content": user_input
        })

        response = ask_llm(messages)

        print(f"ADAM: {response}\n")

        messages.append({
            "role": "assistant",
            "content": response
        })


if __name__ == "__main__":
    main()
