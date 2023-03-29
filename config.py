from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "25843661"))
API_HASH = getenv("API_HASH", "5e5bdce7ff26e46d224d62298850dec8")
BOT_TOKEN = getenv("BOT_TOKEN", "6107856966:AAEFb3iNHHzpuEeneQhi6NsEugLlcjCequ4")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
