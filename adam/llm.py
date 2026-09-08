import requests


SERVER_URL = "http://127.0.0.1:8080"


def ask_llm(prompt):
    response = requests.post(
        f"{SERVER_URL}/completion",
        json={
            "prompt": prompt,
            "n_predict": 128
        },
        timeout=120
    )

    response.raise_for_status()

    data = response.json()
    return data["content"].strip()
