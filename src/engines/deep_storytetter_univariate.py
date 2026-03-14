client = OpenAI()
# Deep Storyteller
def deep_storyteller(base_interpretation, tool_results, problem_context):

    import time
    import json
    
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

Base Interpretation:
{base_interpretation}

Additional Evidence from Analysis Tools:
{tool_results}

Task:
Extend the base interpretation using the additional evidence.

Guidelines:
- Do NOT contradict the base interpretation
- Focus on providing response only for the newer analysis as indicated by the the tool plan
- Make sure all the analysis mentioned in the tool plan is covered.
- Add the reason why these newer evidences are added and blend it into the story
- Use tool results to strengthen or clarify observations
- Explicitly reference key statistics (percentiles, counts, etc.) where relevant
- Keep the narrative natural and easy to read
- Do NOT introduce new assumptions, causes, or relationships
- Stay strictly within this variable
- Keep it concise (5-7 sentences)
- Frame around the real-world entity

Write the explanation as if you are walking a reader through the charts
and helping them notice what stands out. Focus on describing the
observable patterns in a natural narrative rather than listing
statistical properties.


FRAME THE EXPLANATION AROUND THE ENTITY DESCRIBED IN THE PROBLEM CONTEXT RATHER THAN REPEATEDLY REFERRING TO "THE DISTRIBUTION".

OUTPUT FORMAT:
Return ONLY the final narrative text. No JSON.
"""
                    }
                ]
            }
        ]
    )

    latency = time.time() - start_time

    narrative = response.output_text.strip()

    return narrative, latency
