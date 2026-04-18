from google import genai
import os
from dotenv import load_dotenv

load_dotenv()

my_api_key = os.environ.get("GEMINI_API_KEY")

client = genai.Client(
        api_key=my_api_key
    )

def code_debugger(images, option): # option will be "Debug Code", "Explain Code", "Optimize Code"
    prompt = f"""
            You are an expert code assistant. Your task is to analyze the content of the provided images and perform the following action based on the selected option: {option}. Please carefully review the code snippets in the images and provide a detailed response that addresses the selected option effectively.
            """
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text
