import requests

url = "https://1a6b7b24135923be-example.runsync.novita.dev/v1/chat/completions"

headers = {"Content-Type": "application/json"}

data = {
    "model": "meta-llama/Llama-3.1-8B-Instruct",
    "messages": [
        {"role": "system", "content": "Act like you are a helpful assistant."},
        {"role": "user", "content": "what is the capital of india"},
    ],
    "max_tokens": 512,
}

response = requests.post(url, headers=headers, json=data)

print(response.json()["choices"][0]["message"]["content"])
