
CONTROLLER_VERSION = "0.1.0"

def define_problem_statement(problem_description):
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
  for i in range(5):
    question = questions_.split("\n")[i].strip()
    print(question)
    answer = input("Enter your answer: ")
    print("\n")

    feedback_ = feedback_generator_ps(story_, question, answer)
    feedback_json = json.loads(feedback_)

    qa_pairs[i] = {"question": question, "answer": answer, "feedback": feedback_json["Feedback"], "refined_answer": feedback_json["Refined_Version"]}

    display(Markdown(feedback_json["Feedback"]))
    display(Markdown(feedback_json["Refined_Version"]))
    print("\n")

  #The final step - the problem statement
  print("\n")
  print("Final Problem Statement")
  print("\n")
  problem_statement_ = input("Based on the above discussions can you give an attempt to frame the problem statement?")

  return({"story": story_, "qa_pairs": qa_pairs, "problem_statement": problem_statement_})
