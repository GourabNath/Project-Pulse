
CONTROLLER_VERSION = "0.1.0"

def define_problem_statement(problem_description):
  from IPython.display import Markdown, display
  #Generate Story
  from src.engines.story_engine import story_generator
  story_ = story_generator(problem_description)
  display(Markdown(story_))
  print("\n\n")

  #Generate Reflection Questions
  from src.engines.reflection_questions_engine import reflection_questions_generate
  questions_ = reflection_questions_generate(story_)

  #This section asks several questions to the user - makes them think - and then refine their thoughts
  import json
  qa_pairs = {}
  qa_pairs_refined = {}
  for i in range(5):
    question = questions_.split("\n")[i].strip()
    print(question)
    answer = input("Enter your answer: ")
    print("\n")

    from src.engines.feedback_engine_ps import feedback_generator_ps
    feedback_ = feedback_generator_ps(story_, question, answer)
    feedback_json = json.loads(feedback_)

    qa_pairs[i] = {"question": question, "answer": answer, "feedback": feedback_json["Feedback"], "refined_answer": feedback_json["Refined_Version"]}
    qa_pairs_refined[i] = {"question": question, "refined_answer": feedback_json["Refined_Version"]}

    display(Markdown(feedback_json["Feedback"]))
    display(Markdown(feedback_json["Refined_Version"]))
    print("\n")

  #The final step - the problem statement
  print("\n")
  print("Final Problem Statement")
  print("\n")
  print('''
  Based on the above discussions can you give an attempt to frame the problem statement?
  Instructions: Try to address the following questions in your problem statement. 
      1. Stakeholder clarity — Is it clear who is affected?
      2. Problem mechanism — Is it clear what is actually going wrong?
      3. Business impact — Does it explain why this matters?
      4. Actionability — Can this realistically lead to an analytical solution?
      5. Alignment — Does it reflect insights discussed in the Q&A and story?
      '''
      )
  print("\n")
  problem_statement_ = input()
  print("\n")

  from src.engines.evaluator_engine_ps import problem_statement_evaluator
  evaluation_ = problem_statement_evaluator(problem_statement_, qa_pairs_refined, story_)
  evaluation_json = json.loads(evaluation_)
  display(Markdown(evaluation_json["Evaluation"]))
  display(Markdown(evaluation_json["Refined Version"]))

  return({"story": story_, "qa_pairs": qa_pairs, "problem_statement": problem_statement_})
