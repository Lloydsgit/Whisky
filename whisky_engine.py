import os
from openai import OpenAI
from prompts import WHISKY_SYSTEM_PROMPT

client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))

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
    return ask_gpt(f"Generate 20 viral hooks about: {input_text}")


def generate_script(input_text):
    return ask_gpt(f"Create a short viral reel script: {input_text}")


def generate_ideas(input_text):
    return ask_gpt(f"Give 10 viral reel ideas: {input_text}")


def generate_viral_pack(input_text):
    return ask_gpt(f"""
    Create a viral pack for: {input_text}
    Include:
    - 20 hooks
    - 3 scripts
    - 5 ideas
    """)


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
        return ask_gpt(user_input)
