import os
import gradio as gr
from langchain_openai import ChatOpenAI

os.environ["OPENAI_API_KEY"] = "ini rahasia"    # buat sendiri -> https://platform.openai.com/api-keys
gpt3 = ChatOpenAI(model_name="gpt-3.5-turbo" )

'''
text = "Berikan fakta menarik tentang kentang!"
print(gpt3.invoke(text).content)
'''

def chatbot(prompt):
    return gpt3.invoke(prompt).content

demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)