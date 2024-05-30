from langchain.llms import HuggingFaceEndpoint
from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
import os
# Your Hugging Face API token    follow this link  https://huggingface.co/settings/tokens
HUGGINGFACEHUB_API_TOKEN = "replace key here"

os.environ["HUGGINGFACEHUB_API_TOKEN"]=HUGGINGFACEHUB_API_TOKEN
# Specify the model repo ID
repo_id = "mistralai/Mistral-7B-Instruct-v0.2"


question = "What is the future AI trends? "

template = """Question: {question}

Answer: Let's think step by step."""

prompt = PromptTemplate.from_template(template)
# Define your prompt template
prompt = PromptTemplate(
    input_variables=["question"],
    template="Question: {question}\nAnswer:"
)

llm = HuggingFaceEndpoint(
    repo_id=repo_id, temperature=0.5, token=HUGGINGFACEHUB_API_TOKEN
)
llm_chain = LLMChain(prompt=prompt, llm=llm)
print(llm_chain.run(question))


