from mlx_lm import load, generate

model, tokenizer, *_ = load("Qwen/Qwen3-1.7B-MLX-4bit")
prompt = "Hello, please introduce yourself and tell me what you can do."

if tokenizer.chat_template is not None:
    messages = [{"role": "user", "content": prompt}]
    prompt = tokenizer.apply_chat_template(
        messages,
        add_generation_prompt=True
    )

response = generate(
    model,
    tokenizer,
    prompt=prompt,
    verbose=True,
    max_tokens=1024
)

print(response)
