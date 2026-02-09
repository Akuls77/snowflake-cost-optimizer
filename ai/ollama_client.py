import subprocess


def call_mistral(prompt: str) -> str:
    """
    Sends a prompt to the local Mistral model via Ollama
    and returns the generated response.
    """

    result = subprocess.run(
        ["ollama", "run", "mistral"],
        input=prompt,
        text=True,
        capture_output=True
    )

    if result.returncode != 0:
        return "Error calling the AI model."

    return result.stdout.strip()
