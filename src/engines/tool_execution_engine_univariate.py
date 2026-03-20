from src.tools.eda_toolset_univariate import *

# Create Tool Registry
TOOLS = {
    "right_tail_percentiles": right_tail_percentiles,
    "left_tail_percentiles": left_tail_percentiles,
    "outlier_analysis": outlier_analysis,
    "bin_distribution": bin_distribution,
    "variability_analysis": variability_analysis,
    "tight_distribution": tight_distribution,
    "missing_analysis": missing_analysis
}

# Tool Execution Engine
def run_tool(tool_name, series):
    '''
    This function runs a specific statistical tool on a given numerical variable
    PARAMNETERS
        tool_name: a tool name from the tool registery
        series: a variable (pandas series object)
    '''

    if tool_name not in TOOLS:
        raise ValueError(f"Tool {tool_name} not recognized")

    tool_function = TOOLS[tool_name]

    result = tool_function(series)

    return result


# Execute Multiple Tools Based on Confidence
def run_selected_tools(series, tool_decisions, threshold=70):

    results = {}

    for tool, info in tool_decisions.items():

        if info["confidence"] >= threshold:
            results[tool] = run_tool(tool, series)

    return results
