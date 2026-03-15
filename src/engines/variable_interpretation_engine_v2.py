
VERSION = 2.0 # Creating a planner inside the variable_interpretation_engine

import os
import json
import base64
import time
from openai import OpenAI


client = OpenAI()

def load_problem_context(path):
    '''
    Load the problem context from the project metadata
    PARAMETER:
        path: the path to the JSON file that stores the project metadata
    '''
    with open(path, "r") as f:
        context = json.load(f)
    return context.get("problem_description", "")



def encode_image(path):
    '''
    Encode image to base64 (convert image to text encoding)
    PARAMETER:
        path: path to the image file
    '''
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")



def load_summary(variable_path):
    '''
    Load the summary statistics of a variable
    PARAMATER:
        variable_path: folder path that contains files (plots, summary) related to the variable. 
    '''
    summary_path = os.path.join(variable_path, "summary.json")
    with open(summary_path, "r") as f:
        return json.load(f)



def get_plot_paths(variable_path):
    '''
    Construct the path to the plots.
    PARAMETERS:
        variable_path: folder path that contains files (plots, summary) related to the variable
    '''
    histogram_path = os.path.join(variable_path, "histogram.png")
    boxplot_path = os.path.join(variable_path, "boxplot.png")
    return histogram_path, boxplot_path



def variable_interpretation_engine(variable_path, problem_context):

    summary = load_summary(variable_path)
    histogram_path, boxplot_path = get_plot_paths(variable_path)

    histogram_b64 = encode_image(histogram_path)
    boxplot_b64 = encode_image(boxplot_path)

    start_time = time.time()

    response = client.responses.create(
        model="gpt-4o",
        input=[
            {
                "role": "user",
                "content": [
                    {
                        "type": "input_text",
                        "text": f"""
You are a professional data analyst.

Problem Context:
{problem_context}

Variable:
{summary['variable']}

Summary Statistics:
{summary}

Task has TWO parts:

---------------------
PART 1 — Interpretation
---------------------
Explain the key observable patterns using histogram, boxplot, and summary.

Guidelines:
- Blend all evidence naturally
- Keep it 4–6 sentences
- Do NOT infer causes or relationships
- Focus only on this variable
- Frame around the real-world entity

FRAME THE EXPLANATION AROUND THE ENTITY DESCRIBED IN THE PROBLEM CONTEXT RATHER THAN REPEATEDLY REFERRING TO "THE DISTRIBUTION".

---------------------
PART 2 — Investigation Planning
---------------------
Based on the interpretation, decide which analyses are needed.

Available tools:
1. right_tail_percentiles
2. left_tail_percentiles
3. outlier_analysis
4. bin_distribution
5. variability_analysis
6. missing_analysis
7. tight_distribution

For EACH tool:
- Assign a confidence score (0–100)
- Provide a short reason

Reason Writing Style:
- Write reasons as natural analytical thoughts, not formal objectives
- Avoid phrases like "to understand", "to analyze", "to evaluate"
- Use observational and curiosity-driven language

Good example:
"The tail of the distribution looks longer towards the right. It would be interesting to see what's happening in the higher range."

Bad example:
"To understand the extent and significance of higher values."

---------------------
OUTPUT FORMAT (STRICT JSON)
---------------------
{{
  "interpretation": "...",
  "tool_plan": {{
    "right_tail_percentiles": {{"confidence": 0, "reason": ""}},
    "left_tail_percentiles": {{"confidence": 0, "reason": ""}},
    "outlier_analysis": {{"confidence": 0, "reason": ""}},
    "bin_distribution": {{"confidence": 0, "reason": ""}},
    "variability_analysis": {{"confidence": 0, "reason": ""}},
    "missing_analysis": {{"confidence": 0, "reason": ""}},
    "tight_distribution": {{"confidence": 0, "reason": ""}}
  }}
}}

Return ONLY valid JSON. Do not include any explanation, markdown, or text outside JSON.
"""
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{histogram_b64}"
                    },
                    {
                        "type": "input_image",
                        "image_url": f"data:image/png;base64,{boxplot_b64}"
                    }
                ]
            }
        ]
    )

    latency = time.time() - start_time

    # Parse JSON safely
    import json
    import re

    raw = response.output_text.strip()

    # Extract JSON block using regex
    match = re.search(r"\{.*\}", raw, re.DOTALL)

    if not match:
        raise ValueError(f"No JSON found in response:\n{raw}")

    json_str = match.group()

    try:
        output = json.loads(json_str)
    except json.JSONDecodeError as e:
        raise ValueError(f"Invalid JSON:\n{json_str}") from e

    interpretation = output["interpretation"]
    tool_plan = output["tool_plan"]

    return interpretation, tool_plan, latency
