from ctransformers import AutoModelForCausalLM
from typing import List
import chainlit as cl

### llm implementation
# step 1
    # (1)load model
    # (2)using single prompt
    # (3)streaming answers
# step 2
    # referring to model prompt format, implementing prompt format correctly
# step 3
    # loading chat memory 

def get_prompt(instruction: str, history: List[str]= []) -> str:
    system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
    prompt = f"### System:\n{system}\n\n### User:\n"
    if len(history) > 0:
        prompt += f"This is the conversatin history: {''.join(history)}. Now answer the question: "
    prompt += f"{instruction}\n\n### Response:\n"
    return prompt


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