from rag import retrieve_context
from llm import llm
from prompt import PROMPT, QUESTION_PROMPT



def diagnose(problem):


    context, confidence = retrieve_context(problem)



    # Generate follow-up questions

    question_prompt = QUESTION_PROMPT.format(
        problem=problem,
        context=context
    )


    questions = llm.invoke(
        question_prompt
    )



    # Generate diagnosis

    final_prompt = PROMPT.format(
        problem=problem,
        context=context + f"""

Retrieval confidence:
{confidence}%

"""
    )



    response = llm.invoke(
        final_prompt
    )


    return {

        "diagnosis": response.content,

        "questions": questions.content,

        "confidence": confidence

    }