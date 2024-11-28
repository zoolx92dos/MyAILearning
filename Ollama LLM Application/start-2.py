# Using ollama library
# pip install ollama

import ollama

# response = ollama.list()
# print(response)

response = ollama.list()


# == Chat Example ==
res = ollama.chat(
    model = "llama3.2",
    messages = [
        {"role": "user", "content": "why is the sky blue?",},
    ]
)

print(res)
print(res["message"]["content"])

# for streaming
res2 = ollama.chat(
    model = "llama3.2",
    messages = [
        {"role": "user", "content": "why is the ocean so salty?",},
    ],
    stream=True,
)
for chunk in res2:
    print(chunk["message"]["content"], end="", flush=True)

# show
print(ollama.show("llama3.2"))


# using model file for specific instruction

modelfile = """
FROM llama3.2
SYSTEM You are very smart assistant who knows everything about oceans. You are very succint and intelligent.

PARAMETER temperature 0.1
"""

ollama.create(model="knowitall", modelfile=modelfile)

res3 = ollama.generate(model="knowitall", prompt="Why is the ocean so salty?")

print(res3["response"])

# delete models
ollama.delete("knowitall")