from src.tools import *
from src.engines.tool_execution_engine_univariate import *
from src.engines.variable_interpretation_engine_v2 import *
from src.engines.deep_storytetter_univariate import deep_storyteller
from src.engines.utils.animation import *

def variable_interpretation_controller(variable_path, prob_context, threshold=80):
    base_interpretation, tool_plan, latency = variable_interpretation_engine(
        variable_path,
        prob_context
    )

    deep_gate = 0
    for tool, info in tool_plan.items():
            if info["confidence"] >= threshold:
              deep_gate = 1
              break

    if deep_gate == 1:
      series = df[variable]
      tool_results = run_selected_tools(series, tool_plan, threshold=threshold)
      deep_story = deep_storyteller(base_interpretation, tool_results, prob_context)
    else:
      deep_story = None

    out = {"base_interpretation": base_interpretation,
          "deep_gate": deep_gate,
          "tool_plan": tool_plan,
          "deep_story": deep_story}

    return out




from concurrent.futures import ThreadPoolExecutor

def interpret_variables_parallel_ai(variable_paths, problem_context, max_workers=5):
    """
    Parallel version of variable interpretation using a simple executor.map pattern.

    Parameters:
        variable_paths (list): List of variable paths
        problem_context (dict/str): Context for interpretation
        max_workers (int): Number of parallel threads

    Returns:
        dict: Mapping of variable_name -> structured interpretation output
    """

    results = {}

    # ThreadPoolExecutor is ideal here assuming I/O-bound work (LLM/tool calls)
    with ThreadPoolExecutor(max_workers=max_workers) as executor:
        
        # Run controller in parallel for all variable paths
        outputs = executor.map(
            lambda path: variable_interpretation_controller(path, problem_context),
            variable_paths
        )

        # Combine inputs with outputs (preserves order)
        for path, result in zip(variable_paths, outputs):
            variable_name = path.split("/")[-1]

            results[variable_name] = result  # result already contains full structured output

    return results


  
from src.engines.utils.typewriter import stream_markdown
import time

def run_variable_interpretation_controller(variable_list, problem_context):  
  start = time.time()
  variable_paths = []
  for variable in variable_list:
    variable_path = run_path + "/" + variable
    variable_paths.append(variable_path)
  
  result = interpret_variables_parallel_ai(variable_paths, prob_context)
  stop = time.time()
  duration = stop - start

  #Print Results
  print("result generated in %f seconds" %duration)
  for variable in variable_list:
    stream_markdown("**"+variable.upper()+"**")
    stream_markdown("---")
    stream_markdown(result[variable]["base_interpretation"])
    print("\n")
    if result[variable]["deep_gate"] == 1:
      thinking_animation()
      stream_markdown('**Planning for a deeper analysis:**')
      for tool, info in result[variable]["tool_plan"].items():
              if info["confidence"] >= 80:
                  time.sleep(0.5)
                  stream_markdown("- " + info['reason'])
      print("\n")
      analyzing_animation()
      stream_markdown('**Deep Analysis**')
      stream_markdown(result[variable]["deep_story"][0])
    stream_markdown("---")
    print("\n")
    print("Press ENTER to continue")
    print("\n")

    input()

  return(result)
