
from src.prompts.problem_statement_evaluaton import system_prompt, build_user_prompt
from src.core.llm_client import generate_response

def problem_statement_evaluator(problem_statement, qa_discussion, story):
  '''
  Descriiption: This function evaluated the user-defined analytical problem statement based on a list of criteria defined in the system prompt.
  Input: this function takes 3 inputs,
    - problem_statement: user-defined problem statement (string).
    - qa_discussion: a dictionary containing the q&a discussions related to the problem statement (dictionary).
    - story: the story related to the problem (string).
  Output: problem evaluation and refined problem statement (string).

  '''
  messages = [
    {"role": "system", "content": system_prompt},
    {"role": "user", "content": build_user_prompt(problem_statement, qa_discussion, story)}
  ]
  return generate_response(messages)

