from langchain.chains import LLMChain
from langchain.prompts import PromptTemplate
from langchain.llms import OpenAI  # or Hugging Face model

llm = OpenAI(temperature=0.9)  # You can replace this with Hugging Face model

template = """You're a teacher using the Socratic method.
Given the student's response: {response}, ask a probing question to lead the student to the correct understanding."""

prompt = PromptTemplate(input_variables=["response"], template=template)
chain = LLMChain(llm=llm, prompt=prompt)

def generate_question(response: str):
    return chain.run(response)
