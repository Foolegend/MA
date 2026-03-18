from ollama import embed

response = embed(model='qwen3-embedding:4b', input='Hello, world!')
print(response['embeddings'])

response = embed(model='llama3.2:3b', input='Hello, world!')
print(response['embeddings'])
