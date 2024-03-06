import os
import gradio as gr
from langchain_community.llms import HuggingFaceEndpoint

os.environ["HUGGINGFACEHUB_API_TOKEN"] = "ini rahasia"  # buat sendiri -> https://huggingface.co/
llm = HuggingFaceEndpoint(repo_id="google/flan-ul2")

'''
text = "ini tanggal berapa?"
result = llm.invoke(text)
print(result)
'''

def chatbot(prompt):
    return llm.invoke(prompt)

# Membuat antarmuka Gradio untuk fungsi chatbot
demo = gr.Interface(fn=chatbot, inputs="text", outputs="text")
demo.launch(server_name="0.0.0.0", server_port= 7860, share=True)