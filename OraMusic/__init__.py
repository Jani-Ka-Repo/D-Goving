from OraMusic.core.bot import Lucky
from OraMusic.core.dir import dirr
from OraMusic.core.git import git
from OraMusic.core.userbot import Userbot
from OraMusic.misc import dbb, heroku
from pyrogram import Client
from SafoneAPI import SafoneAPI
from .logging import LOGGER

dirr()
git()
dbb()
heroku()

app = Lucky()
api = SafoneAPI()
userbot = Userbot()

from .platforms import *

Apple = AppleAPI()
Carbon = CarbonAPI()
SoundCloud = SoundAPI()
Spotify = SpotifyAPI()
Resso = RessoAPI()
Telegram = TeleAPI()
YouTube = YouTubeAPI()
