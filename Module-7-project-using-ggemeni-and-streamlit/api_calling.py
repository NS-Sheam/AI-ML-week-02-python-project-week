from google import genai
from dotenv import load_dotenv
import os



# load environment variables from .env file

load_dotenv()

my_api_key = os.environ.get("GEMENI_API_KEY")

# initialize the Gemini client with the API key

client = genai.Client(api_key=my_api_key)


# note generation function

def note_generator(images):
    prompt = """
            You are an expert note summarizer. Your task is to analyze the content of the provided images and generate concise notes based on the information depicted in them. Please summarize the key points and information from the images in a clear and organized manner, using approximately 100 words.
            """
    response = client.models.generate_content(
        model="gemini-3-flash-preview",
        contents=[images, prompt]
    )
    return response.text