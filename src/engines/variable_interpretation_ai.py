
# AI-Interpretation of graphs and summary
import os
import json
import base64
import time
from openai import OpenAI


client = OpenAI()

def load_problem_context(path):
    with open(path, "r") as f:
        context = json.load(f)
    return context.get("problem_description", "")

def encode_image(path):
    with open(path, "rb") as image_file:
        return base64.b64encode(image_file.read()).decode("utf-8")


def load_summary(variable_path):
    summary_path = os.path.join(variable_path, "summary.json")
    with open(summary_path, "r") as f:
        return json.load(f)


def get_plot_paths(variable_path):
    histogram_path = os.path.join(variable_path, "histogram.png")
    boxplot_path = os.path.join(variable_path, "boxplot.png")
    return histogram_path, boxplot_path


def variable_interpretation_engine(variable_path, problem_context):

    # Load summary
    summary = load_summary(variable_path)

    # Get plot paths
    histogram_path, boxplot_path = get_plot_paths(variable_path)

    # Encode images
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

Variable: {summary['variable']}

Summary Statistics:
{summary}

You are a professional data analyst helping users interpret exploratory data analysis.

Variable:
{summary['variable']}

Summary Statistics:
{summary}

Interpret the distribution of a single variable using the histogram,
boxplot, and summary statistics as evidence.

First identify the most distinctive characteristic of the distribution
(e.g., concentration, skew, spread, clustering, or outliers).
Build the explanation around this observation.

Blend evidence from the histogram, boxplot, and statistics naturally
rather than describing each chart separately.

Focus on describing how the values are distributed rather than
describing the charts themselves.

Guidelines:

- Lead with the most noticeable pattern in the variable.
- Use statistics only to support an observation.
- Mention charts only when they strengthen the explanation.
- Do not describe the histogram or boxplot step-by-step.
- Do not speculate about causes, roles, outcomes, or business meaning.
- Refer to the dataset or records rather than assuming real-world roles.
- Use vivid analytical language such as "cluster", "spread", "extend",
  "concentrate", or "taper" instead of generic phrases like
  "the histogram shows".

Keep the explanation concise (4–6 sentences).

End with a short observation about what this variable reveals about
the range or variability present in the dataset.

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
    interpretation = response.output_text

    return interpretation, latency
