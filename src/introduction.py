
from llm_client import generate_response
from prompts.introduction_prompt import build_introduction_messages


def get_introduction(project_name, project_description):

    messages = build_introduction_messages(
        project_name,
        project_description
    )

    return generate_response(messages)
