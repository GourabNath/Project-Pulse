# Parallel processing
from concurrent.futures import ThreadPoolExecutor
import src.engines.variable_interpretation_ai as vi

def interpret_variables_parallel(variable_paths, problem_context, max_workers=5):

    # This dictionary will store the results of each variable interpretation
    # Example structure:
    # {
    #   "variable1": {"interpretation": "...", "latency": 7.3},
    #   "variable2": {"interpretation": "...", "latency": 6.8}
    # }
    results = {}

    # ThreadPoolExecutor manages a pool of worker threads.
    # Each thread will run one API call (interpret_variable).
    # max_workers defines how many threads can run at the same time.
    # For 5 variables, 5 workers means they can all run simultaneously.
    with ThreadPoolExecutor(max_workers=max_workers) as executor:

        # executor.map() runs the function for each element in variable_paths.
        # Each variable_path gets sent to interpret_variable().
        #
        # IMPORTANT:
        # We pass problem_context to every call using a lambda wrapper.
        #
        # This line starts all threads immediately.
        outputs = executor.map(
            lambda path: vi.interpret_variable(path, problem_context),
            variable_paths
        )

        # executor.map() returns results in the SAME ORDER as input.
        # So the first output corresponds to the first variable_path.
        for path, result in zip(variable_paths, outputs):

            # Extract the variable name from the path
            # Example:
            # "runs/run_001/Age" -> "Age"
            variable_name = path.split("/")[-1]

            interpretation, latency = result

            # Store result inside dictionary
            results[variable_name] = {
                "interpretation": interpretation,
                "latency": latency
            }

    # Once all threads finish, we return the dictionary
    return results
