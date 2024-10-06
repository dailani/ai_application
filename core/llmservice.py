import os
from openai import OpenAI

from dotenv import load_dotenv

load_dotenv(override=True)


def generate_llm_response(input_text):
    # Ensure you've set your OpenAI API key in an environment variable
    client = OpenAI(api_key=os.environ.get("OPENAI_API_KEY"))


    # Start the streaming process with the custom input_text
    stream = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[{"role": "user", "content": input_text}],
        stream=True,
    )

    # Yield each chunk of the streamed response
    for chunk in stream:
        if chunk.choices[0].delta.content is not None:
            yield chunk.choices[0].delta.content