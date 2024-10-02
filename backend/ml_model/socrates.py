
import google.generativeai as genai
import os

genai.configure(api_key=os.environ["GEMINI_API_KEY"])

Model = genai.GenerativeModel(
    'gemini-1.5-flash',
    generation_config=genai.GenerationConfig(
        max_output_tokens=100,
        temperature=0.5,
    ),
    system_instruction='You are a teacher and you teach using socrates method, make converstaions to students with the intent to make them understand concepts'
)

   
async def giveSentimentDescription(context:str):
    return await Model.generate_content_async(f'{context}')