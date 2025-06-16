import requests

OLLAMA_URL = "http://localhost:11434/api/generate"
MODEL_NAME = "tinyllama"  # Make sure this is pulled via `ollama pull tinyllama`

def generate_recipe(ingredients: list[str]) -> str:
    prompt = (
        "You are a helpful cooking assistant.\n"
        f"Suggest 3 simple recipes using only these ingredients:\n"
        f"{', '.join(ingredients)}.\n"
        "Keep it short, simple, and beginner-friendly.\n"
        "List them clearly."
    )

    response = requests.post(
        OLLAMA_URL,
        json={
            "model": MODEL_NAME,
            "prompt": prompt,
            "stream": False
        }
    )

    if response.status_code != 200:
        raise Exception(f"Ollama API error: {response.text}")

    data = response.json()
    return data.get("response", "").strip()
