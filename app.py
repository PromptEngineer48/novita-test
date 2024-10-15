from openai import OpenAI

client = OpenAI(
    base_url="https://api.novita.ai/v3/openai",
    # Get the Novita AI API Key by referring to: https://novita.ai/docs/get-started/quickstart.html#_2-manage-api-key.
    api_key="a2bfde9b-3623-45cc-bf15-9d96c0442fbf",
)

model = "meta-llama/llama-3.1-8b-instruct"
stream = False  # or False
max_tokens = 512

chat_completion_res = client.chat.completions.create(
    model=model,
    messages=[
        {
            "role": "system",
            "content": "Act like you are a helpful assistant.",
        },
        {
            "role": "user",
            "content": "What is the capital of India?",
        },
    ],
    stream=stream,
    max_tokens=max_tokens,
)

if stream:
    for chunk in chat_completion_res:
        print(chunk.choices[0].delta.content or "", end="")
else:
    print(chat_completion_res.choices[0].message.content)
