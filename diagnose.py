from rag import retrieve_context
from llm import llm
from prompt import PROMPT


def diagnose(problem):

    context = retrieve_context(problem)


    final_prompt = PROMPT.format(
        problem=problem,
        context=context
    )


    response = llm.invoke(final_prompt)


    return response.content