from src.prompts.story import SYSTEM_PROMPT, build_user_prompt
from src.llm_client import generate_response


def story_generator(problem_description: str) -> str:
    '''
    Description: this function helps in generating a fictitious user story for a given problem description
    Input: the function takes only one input
        - problem_description: a small introduction or description of the problem of interest (str)
    Output: a generated story  for the problem of interest (str).

    '''
    messages = [
        {"role": "system", "content": SYSTEM_PROMPT},
        {"role": "user", "content": build_user_prompt(problem_description)}
    ]

    return generate_response(messages)
