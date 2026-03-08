from src.prompts.feedback_and_finetune import build_system_prompt, build_user_prompt
from src.llm_client import generate_response

def feedback_generator_ps(problem_context, question, answer) -> str:
  '''
  Description: This function evaluated user response for a reflecting question.
  Input: 
    problem_context: a story related to the problem (str).
    question: a system generated reflecting question related to the problem (str).
    answer: the answer entered by the user corresponding to the question (str).
  Output: evaluation of the answer and finetuned response (str).
  '''
  messages = [
      {"role": "system", "content": build_system_prompt(problem_context, question)},
      {"role": "user", "content": build_user_prompt(answer)}
  ]

  return(generate_response(messages))
