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

### chat UI chainlit
# customize UI chat function - to integrate prompt and response
# move LLM download to UI chat session initialization
# streaming in UI
# memory of history (make it seperate for each user) 


def get_prompt(instruction: str, history: List[str]= []) -> str:
    system = "You are an AI assistant that gives helpful answers. You answer the questions in a short and concise way."
    prompt = f"### System:\n{system}\n\n### User:\n"
    if len(history) > 0:
        prompt += f"This is the conversatin history: {''.join(history)}. Now answer the question: "
    prompt += f"{instruction}\n\n### Response:\n"
    return prompt

@cl.on_message
async def on_message(message: cl.Message):
    message_history = cl.user_session.get("message_history")
    msg = cl.Message(content="")
    await msg.send()

    prompt = get_prompt(message.content, message_history)
    
    response=""
    for word in llm(prompt, stream=True):
        await msg.stream_token(word)
        response += word
    await msg.update()
    message_history.append(response) 

@cl.on_chat_start
def on_chat_start():
    cl.user_session.set("message_history", [])
    global llm
    llm = AutoModelForCausalLM.from_pretrained(
        "zoltanctoth/orca_mini_3B-GGUF", model_file="orca-mini-3b.q4_0.gguf"
    )
    print("A new chat session has started!")



# for original local chat 
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