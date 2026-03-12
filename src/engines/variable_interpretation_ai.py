
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


def interpret_variable_engine(variable_path, problem_context):

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

Analyze the histogram and boxplot along with the statistics.

Write a concise professional paragraph describing:
- distribution shape
- presence of outliers
- notable characteristics
- possible implications for the business problem.
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
