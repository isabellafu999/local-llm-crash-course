from ctransformers import AutoModelForCausalLM
from typing import List
import chainlit as cl

# load model
# using single prompt
# streaming answers
# referring to model prompt format, implementing prompt format correctly
# loading chat memory 

llm = AutoModelForCausalLM.from_pretrained(
        "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
    )

def get_prompt(instruction: str, history: List[str]) -> str:
    system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
    prompt = f"### System:\n{system}\n\n### User:\n"
    if history is not None:
        prompt += f"This is the conversatin history: {''.join(history)}. Now answer the question: "
    prompt += f"{instruction}\n\n### Response:\n"
    print(prompt)
    return prompt

@cl.on_message
async def on_message(message: cl.Message):
    response = f"Hello, you just sent: {message.content}!"
    await cl.Message(response).send()

"""
history = []

# question 1
question="Which city is the capital of India ?"

answer = ""
for word in llm(get_prompt(question, history), stream=True):
    print(word, end="", flush=True)
    answer += word
print()

history.append(answer)

# question 2
question="And which is of the United States ?"

answer = ""
for word in llm(get_prompt(question, history), stream=True):
    print(word, end="", flush=True)
    answer += word
print()

history.append(answer)
"""