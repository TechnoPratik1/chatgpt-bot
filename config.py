from os import getenv
from dotenv import load_dotenv

load_dotenv("config.env")

API_ID = int(getenv("API_ID", "25843661"))
API_HASH = getenv("API_HASH", "5e5bdce7ff26e46d224d62298850dec8")
BOT_TOKEN = getenv("BOT_TOKEN", "6200553989:AAE5ROwTGD0i91beW7Sw9iL5HVgyeyQ2WHA")
OPENAI_API = getenv("OPENAI_API", "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") # get api key : https://platform.openai.com/account/api-keys
