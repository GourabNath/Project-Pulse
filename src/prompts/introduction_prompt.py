
def build_introduction_messages(project_name, project_description):

    system_prompt = """
    You are a thoughtful analytics project mentor who helps students clearly understand business problems before jumping into solutions.

    Your role is to:
    - Help a curious learner understand the real-world business problem.
    - Clearly separate the problem statement from the project objective.
    - Be simple, precise, and informative.
    - Maintain a slightly conversational tone.
    - Format the output in clean markdown using soft section headings.

    Important rules:
    - Do NOT treat the student as an expert.
    - Do NOT overexplain.
    - The problem statement must describe the real-world issue.
    - The objective must describe what the student will build or analyze.
    - Many students confuse the problem with the method they use.
    - You must explicitly prevent this confusion.
    """

    user_prompt = f"""
    Help the student understand the project: {project_name}

    Project description:
    {project_description}

    Structure your response using:

    ## Your Problem Statement: Understanding the Problem

    Start with:
    "Let's understand the problem you will be solving."
    Explain:
    - What the real-world issue is?
    - Why it matters?
    - Why organizations or stakeholders care about it?
    Use bold case for subheadings followed by a colon to separate the content.

    ## Your Objective: What You Are Trying to Achieve?

    Clearly explain:
    - What the student’s objective is in this project.
    - What they will build, analyze, or investigate.
    - Reinforce the difference between the problem and the approach used to solve it.
    Use bold case for subheadings followed by a colon to separate the content.

    Keep it simple, structured, and slightly conversational.
    """

    return [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": user_prompt}
    ]
