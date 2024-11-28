import requests
import json

url = "http://localhost:11434/api/generate"

data = {
    "model": "llama3.2",
    "prompt": "tell me a short story and make it funny",
}

response = requests.post(url, json=data, stream=True)

# check the response status
if response.status_code == 200:
    print("Generated text:", end=" ", flush=True)
    # Iterate over the streaming response
    for line in response.iter_lines():
        # Decode the line and parse the JSON
        decoded_line = line.decode("utf-8")
        result = json.loads(decoded_line)
        # get the text from the response
        generated_text = result.get("response", "")
        print(generated_text, end="", flush=True)
else:
    print("Error:", response.status_code, response.text)