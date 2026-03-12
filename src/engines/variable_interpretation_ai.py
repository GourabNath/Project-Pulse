
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

Use the histogram, boxplot, and summary statistics together to explain the most noticeable patterns in the variable.
Blend these sources of evidence naturally in the narrative rather than discussing them separately. 
Do not describe the histogram, boxplot, and statistics in separate sentences unless necessary.
Integrate them naturally while explaining the observed pattern.
Prioritize describing what stands out in the variable before mentioning specific charts or statistics.

Guidelines:
- Explain the key patterns visible in the histogram and boxplot.
- Use the summary statistics to support the explanation.
- Connect the observed patterns to the entity described in the problem context so the explanation feels grounded in the real-world scenario.
- Keep the explanation short (about 4–6 sentences).
- Do NOT infer causes, outcomes, or relationships with other variables.
- Limit the explanation strictly to what can be observed in this single variable.

Write the explanation as if you are walking a reader through the charts
and helping them notice what stands out. Focus on describing the
observable patterns in a natural narrative rather than listing
statistical properties.

Use statistics only to support an observation, not as the main focus
of the sentence.

End the explanation by summarizing what the variable reveals about the dataset itself.
Do not connect the observation to outcomes, performance, or business results.

Frame the explanation around the entity described in the problem context rather than repeatedly referring to "the distribution".

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
