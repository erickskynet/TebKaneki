import os
from os import getenv
from dotenv import load_dotenv

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "𝗧𝗲𝗯 𝗞𝗮𝗻𝗲𝗸𝗶 𝗠𝘂𝘀𝗶𝗰")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/49ac0c33e0f9466934427.jpg")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/102b3344faea1dfa30030.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/d477bb9715d2327870ceb.png")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/75f063ee5597867733c52.jpg")
admins = {}
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "TebErickMusik_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "TebAssistentMusicBot")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "TebBotSupport")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "TebMusicUpdate")
OWNER_NAME = getenv("OWNER_NAME", "Cyberhunt27") # isi dengan username kamu tanpa simbol @
DEV_NAME = getenv("DEV_NAME", "Cyberhunt27")
PMPERMIT = getenv("PMPERMIT", None)

DURATION_LIMIT = int(getenv("DURATION_LIMIT", "180"))

COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())

SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
