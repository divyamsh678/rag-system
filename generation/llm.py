import os
from dotenv import load_dotenv
from langchain_openai import ChatOpenAI

load_dotenv()

class LLM:
    def __init__(self,model="Qwen/Qwen3.5-35B-A3B:novita"):
        self.llm=ChatOpenAI(base_url="https://router.huggingface.co/v1",api_key=os.environ["HF_TOKEN"],model=model,temperature=0)
    def generate(self,prompt):
        response=self.llm.invoke(prompt)
        return response.content