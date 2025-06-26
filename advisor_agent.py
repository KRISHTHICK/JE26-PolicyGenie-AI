import subprocess

def get_custom_advice(prompt):
    full_prompt = f"You are an insurance advisor. {prompt} Provide a clear answer."
    result = subprocess.run(["ollama", "run", "tinyllama", full_prompt], capture_output=True, text=True)
    return result.stdout.strip()
