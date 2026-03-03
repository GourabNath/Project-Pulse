from src.prompts.feedback_and_finetune import build_system_prompt, build_user_prompt
from src.llm_client import generate_response

def feedback_generator_ps(problem_context, question, answer) -> str:

  messages = [
      {"role": "system", "content": build_system_prompt(problem_context, question)t},
      {"role": "user", "content": build_user_prompt(answer)}
  ]

  return(generate_response(messages))
