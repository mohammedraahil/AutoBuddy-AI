from rag import retrieve_context
from llm import llm
from prompt import PROMPT


def diagnose(problem):

    context, confidence = retrieve_context(problem)


    final_prompt = PROMPT.format(
    problem=problem,
    context=context + f"""

Retrieval confidence:
{confidence}%

"""
)


    response = llm.invoke(final_prompt)


    return response.content