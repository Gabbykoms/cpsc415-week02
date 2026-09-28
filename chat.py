import os
import json
import urllib.request
import urllib.error

DEFAULT_BASE_URL = "https://openrouter.ai/api/v1"
DEFAULT_MODEL = "openai/gpt-4o-mini"

api_key = os.environ.get("OPENROUTER_API_KEY", "")
base_url = os.environ.get("CHAT_BASE_URL")
model = os.environ.get("CHAT_MODEL")

if not base_url:
    print(f"CHAT_BASE_URL not set, using default: {DEFAULT_BASE_URL}")
    base_url = DEFAULT_BASE_URL

if not model:
    print(f"CHAT_MODEL not set, using default: {DEFAULT_MODEL}")
    model = DEFAULT_MODEL

if not api_key:
    print("Warning: OPENROUTER_API_KEY not set. Requests will likely fail.")

endpoint = f"{base_url}/chat/completions"

print("Chat client ready. Type 'quit' to exit.\n")

while True:
    try:
        question = input("You: ").strip()
    except (EOFError, KeyboardInterrupt):
        print("\nGoodbye.")
        break

    if question.lower() == "quit":
        print("Goodbye.")
        break

    if not question:
        continue

    payload = json.dumps({
        "model": model,
        "messages": [
            {"role": "user", "content": question}
        ],
        "max_tokens": 1024
    }).encode("utf-8")

    req = urllib.request.Request(
        endpoint,
        data=payload,
        headers={
            "Authorization": f"Bearer {api_key}",
            "Content-Type": "application/json"
        },
        method="POST"
    )

    try:
        with urllib.request.urlopen(req) as resp:
            data = json.loads(resp.read().decode("utf-8"))
    except urllib.error.HTTPError as e:
        print(f"HTTP error {e.code}: {e.read().decode('utf-8')}\n")
        continue
    except urllib.error.URLError as e:
        print(f"Connection error: {e.reason}\n")
        continue

    answer = data["choices"][0]["message"]["content"]
    used_model = data.get("model", model)
    usage = data.get("usage", {})
    input_tokens = usage.get("prompt_tokens", "unavailable")
    output_tokens = usage.get("completion_tokens", "unavailable")

    thinking_effort = data["choices"][0]["message"].get("thinking_effort")
    if thinking_effort is None:
        thinking_effort = "No thinking effort label available"

    print(f"\nAssistant: {answer}")
    print(f"\n[Model: {used_model} | Input tokens: {input_tokens} | Output tokens: {output_tokens} | Thinking effort: {thinking_effort}]\n")
