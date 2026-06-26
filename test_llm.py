from llm import llm


response = llm.invoke(
    "Explain why a car AC becomes weak in traffic"
)


print(response.content)