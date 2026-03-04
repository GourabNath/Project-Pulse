
from src.prompts.problem_statement_evaluaton import system_prompt, build_user_prompt

def problem_statement_evaluator(problem_statement, qa_discussion, story):
  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": build_user_prompt(problem_statement, qa_discussion, story)}
  ]
  return generate_response(messages)

