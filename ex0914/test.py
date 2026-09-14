from dotenv import load_dotenv
import os

load_dotenv(".env", override=True)

print("OpenAI:", os.getenv("OPENAI_API_KEY")[:8] + "...")
print("LangSmith:", os.getenv("LANGSMITH_API_KEY")[:8] + "...")
print("Endpoint:", os.getenv("LANGSMITH_ENDPOINT"))
print("Project:", os.getenv("LANGSMITH_PROJECT"))
print("Tracing:", os.getenv("LANGSMITH_TRACING"))