
from src.prompts.reflection_questions import system_prompt, build_user_prompt
from src.core.llm_client import generate_response


def reflection_questions_generate(story: str) -> str:
    '''
    Description: this function generated around 3-5 reflecting questions related to the problem of interest.
    Input: the function takes one input,
        - story: a story related to the problem of interest (str)
    Output: 3-5 reflecting questions as per the instructions given in the system prompt.
    '''
    messages = [
      {"role": "system", "content": system_prompt},
      {"role": "user", "content": build_user_prompt(story)}
    ]
    return generate_response(messages)
