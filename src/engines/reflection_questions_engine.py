
from src.prompts.reflection_questions import system_prompt, build_user_prompt
from src.llm_client import generate_response


def reflection_questions_generate(story: str) -> str:
    messages = [
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": build_user_prompt(story)}
    ]
    return generate_response(messages)
