import os
from google import genai

def make_client():
    api_key = os.getenv("GOOGLE_API_KEY")
    if not api_key:
        raise EnvironmentError("Missing GOOGLE_API_KEY")

    model = os.getenv("MODEL", "gemini-2.5-flash")
    genai.client = genai.Client(api_key=api_key)
    return genai.client, model

def generate_text(prompt: str, max_output_tokens: int = 512) -> str:
    client, model = make_client()
    response = client.models.generate_content(model=model, contents=prompt, max_output_tokens=max_output_tokens)
    return response.text if hasattr(response, "text") else str(response)
