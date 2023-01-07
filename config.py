import os

API_ID = int(os.environ.get("API_ID", 10819555))
API_HASH = os.environ.get("API_HASH", a2f9cab9712c7284afda1f21a778ff15)
BOT_TOKEN = os.environ.get("BOT_TOKEN", None)
DB_CHANNEL_ID = os.environ.get("DB_CHANNEL_ID", -1001516716257)
IS_PRIVATE = os.environ.get("IS_PRIVATE",TRUE) # any input is ok But True preferable
OWNER_ID = int(os.environ.get("OWNER_ID", 1075808797))
PROTECT_CONTENT = True
UPDATE_CHANNEL = os.environ.get('UPDATE_CHANNEL', '')
AUTH_USERS = list(int(i) for i in os.environ.get("AUTH_USERS", "").split(" ")) if os.environ.get("AUTH_USERS") else []
if OWNER_ID not in AUTH_USERS:
    AUTH_USERS.append(OWNER_ID)
