
CONTROLLER_VERSION = "0.1.0"

def define_problem_statement(problem_description):
  from IPython.display import Markdown, display
  from src.typewritter_effect import stream_markdown
  #Generate Story
  from src.engines.story_engine import story_generator
  story_ = story_generator(problem_description)
  stream_markdown(story_)
  print("\n")

  #Generate Reflection Questions
  from src.engines.reflection_questions_engine import reflection_questions_generate
  questions_ = reflection_questions_generate(story_)

  #This section asks several questions to the user - makes them think - and then refine their thoughts
  import json
  qa_pairs = {}
  #qa_pairs_refined = {}

  #Intrtuctions
  instructions = '''
  Before we move ahead, we’ll pause for a moment and reflect on a few business questions related to the story you just read.

  You’ll see these questions one at a time. Take a moment to think about them and write down whatever comes to mind.
  
  There are no perfect answers here. The goal is simply to explore the situation and see what you notice.
  
  If a question feels difficult or you’re unsure, that’s completely okay — you can simply type **PASS** and move on to the next one.
  
  But if you do give it a try, you might find it to be a fun little exercise in thinking like a business analyst.
  '''
  stream_markdown(instructions)

  for i in range(5):
    question = questions_.split("\n")[i].strip()
    stream_markdown(question)
    answer = input()
    print("\n")

    from src.engines.feedback_engine_ps import feedback_generator_ps
    feedback_ = feedback_generator_ps(story_, question, answer)
    #feedback_json = json.loads(feedback_)

    qa_pairs[i] = {"question": question, "answer": answer, "feedback": feedback_}
    #qa_pairs_refined[i] = {"question": question, "refined_answer": feedback_}

    stream_markdown(feedback_)
    #stream_markdown(feedback_json["Feedback"])
    #stream_markdown(feedback_json["Refined_Version"])
    print("\n")

  #The final step - the problem statement
  print("\n")
  stream_markdown("Final Problem Statement")
  print("\n")
  stream_markdown('''
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
  stream_markdown(evaluation_json["Evaluation"])
  stream_markdown(evaluation_json["Refined Version"])

  return({"story": story_, "qa_pairs": qa_pairs, "problem_statement": problem_statement_})
