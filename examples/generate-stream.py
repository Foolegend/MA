from ollama import generate

for part in generate('qwen3.5:0.8b', 'Why is the sky blue?', stream=True):
  print(part['response'], end='', flush=True)
