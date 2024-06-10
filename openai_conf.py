import os
from dotenv import load_dotenv

os.environ["AZURE_OPENAI_API_KEY"] = os.environ["OPENAI_API_KEY"]
os.environ["AZURE_OPENAI_ENDPOINT"] = "https://ai-ser-us.openai.azure.com/"
os.environ["AZURE_OPENAI_API_VERSION"] = "2023-06-01-preview"
os.environ["AZURE_OPENAI_CHAT_DEPLOYMENT_NAME"] = "ai-ser-openai"

load_dotenv()