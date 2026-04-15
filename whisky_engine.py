import os
from openai import OpenAI

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

def process_command(user_input):
    if "/hooks" in user_input:
        return generate_hooks(user_input)
    elif "/script" in user_input:
        return generate_script(user_input)
    elif "/ideas" in user_input:
        return generate_ideas(user_input)
    elif "/viral pack" in user_input:
        return generate_viral_pack(user_input)
    else:
        return general_response(user_input)


def ask_gpt(prompt):
    response = client.chat.completions.create(
        model="gpt-4.1-mini",
        messages=[
            {"role": "system", "content": WHISKY_SYSTEM_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.9
    )
    return response.choices[0].message.content


def generate_hooks(input_text):
    prompt = f"Generate 30 viral hooks based on: {input_text}"
    return ask_gpt(prompt)


def generate_script(input_text):
    prompt = f"Create a short viral Instagram reel script: {input_text}"
    return ask_gpt(prompt)


def generate_ideas(input_text):
    prompt = f"Give 10 viral reel ideas: {input_text}"
    return ask_gpt(prompt)


def generate_viral_pack(input_text):
    prompt = f"""
    Create a viral pack for: {input_text}
    Include:
    - 20 hooks
    - 3 scripts
    - 5 ideas
    """
    return ask_gpt(prompt)


def general_response(input_text):
    return ask_gpt(input_text)
