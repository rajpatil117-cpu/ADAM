import requests


SERVER_URL = "http://127.0.0.1:8080"


def ask_llm(messages):
    response = requests.post(
        f"{SERVER_URL}/v1/chat/completions",
        json={
            "messages": messages,
            "max_tokens": 128,
            "temperature": 0.7,
            "chat_template_kwargs": {
                "enable_thinking": False
            }
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()

    return data["choices"][0]["message"]["content"].strip()
