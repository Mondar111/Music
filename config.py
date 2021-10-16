import os
from os import getenv

from dotenv import load_dotenv

from helpers.uptools import fetch_heroku_git_url

if os.path.exists("local.env"):
    load_dotenv("local.env")

load_dotenv()
que = {}
admins = {}
SESSION_NAME = getenv("SESSION_NAME", "session")
BOT_TOKEN = getenv("BOT_TOKEN")
BOT_NAME = getenv("BOT_NAME", "asistent mon")
BG_IMAGE = getenv("BG_IMAGE", "https://telegra.ph/file/280ad48194ac018699ca2.png")
THUMB_IMG = getenv("THUMB_IMG", "https://telegra.ph/file/70a9f9cd0e3dcf20f5f68.jpg")
AUD_IMG = getenv("AUD_IMG", "https://telegra.ph/file/844a9d79b78c35f129a0e.jpg")
QUE_IMG = getenv("QUE_IMG", "https://telegra.ph/file/fe4c1aa15fcb201c9b4fa.jpg")
ALIVE_IMG = getenv("ALIVE_IMG", "https://telegra.ph/file/70a9f9cd0e3dcf20f5f68.jpg")
API_ID = int(getenv("API_ID"))
API_HASH = getenv("API_HASH")
BOT_USERNAME = getenv("BOT_USERNAME", "musicmon_bot")
ASSISTANT_NAME = getenv("ASSISTANT_NAME", "asistent mon")
GROUP_SUPPORT = getenv("GROUP_SUPPORT", "siniajaloh")
UPDATES_CHANNEL = getenv("UPDATES_CHANNEL", "familynvn")
# isi dengan username kamu tanpa simbol @
OWNER_NAME = getenv("OWNER_NAME", "monajedah")
# fill with your nickname
ALIVE_NAME = getenv("ALIVE_NAME", "mondar111")
# fill with your id as the owner of the bot
OWNER_ID = int(os.environ.get("OWNER_ID"))
DATABASE_URL = os.environ.get("DATABASE_URL")  # fill with your mongodb url
# make a private channel and get the channel id
LOG_CHANNEL = int(os.environ.get("LOG_CHANNEL"))
# just fill with True or False (optional)
BROADCAST_AS_COPY = bool(os.environ.get("BROADCAST_AS_COPY", "False"))
DURATION_LIMIT = int(getenv("DURATION_LIMIT", "60"))
COMMAND_PREFIXES = list(getenv("COMMAND_PREFIXES", "/ ! .").split())
SUDO_USERS = list(map(int, getenv("SUDO_USERS").split()))
# UPDATER CONFIG
U_BRANCH = "main"
HEROKU_APP_NAME = os.environ.get("HEROKU_APP_NAME", None)
HEROKU_API_KEY = os.environ.get("HEROKU_API_KEY", None)
UPSTREAM_REPO = os.environ.get(
    "UPSTREAM_REPO", "https://github.com/mondar111/Music"
)
HEROKU_URL = fetch_heroku_git_url(HEROKU_API_KEY, HEROKU_APP_NAME)
