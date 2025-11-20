import os
from dotenv import load_dotenv

load_dotenv()

API_KEY = os.getenv("BINANCE_API_KEY", "")
API_SECRET = os.getenv("BINANCE_API_SECRET", "")
TESTNET = os.getenv("BINANCE_TESTNET", "true").lower() in ("1", "true", "yes")

# MOCK MODE => No real API needed
MOCK = os.getenv("MOCK_MODE", "true").lower() in ("1", "true", "yes") or (API_KEY == "" or API_SECRET == "")

LOG_FILE = os.getenv("BOT_LOG_FILE", "bot.log")
