import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    # Bot
    BOT_TOKEN     = os.environ.get("BOT_TOKEN", "")
    API_ID        = int(os.environ.get("API_ID", 0))
    API_HASH      = os.environ.get("API_HASH", "")

    # Owner / Admins
    OWNER_ID      = int(os.environ.get("OWNER_ID", 0))
    SUDO_USERS    = [int(x) for x in os.environ.get("SUDO_USERS", "").split(",") if x.strip().isdigit()]

    # Force Sub
    FSUB_CHANNEL_1 = os.environ.get("FORCE_SUB_CHANNEL_1", "")
    FSUB_CHANNEL_2 = os.environ.get("FORCE_SUB_CHANNEL_2", "")

    # MongoDB
    MONGO_URI     = os.environ.get("MONGO_URI", "")
    DB_NAME       = os.environ.get("DB_NAME", "mirrornexus")

    # Downloads
    DOWNLOAD_DIR  = os.environ.get("DOWNLOAD_DIR", "/tmp/downloads")
    MAX_SPLIT_SIZE= int(os.environ.get("MAX_SPLIT_SIZE", 2_000_000_000))
    WORKERS       = int(os.environ.get("WORKERS", 500))

    # Sticker / Welcome
    STICKER_ID        = os.environ.get("STICKER_ID", "CAACAgIAAxkBAAEQZtFpgEdROhGouBVFD3e0K-YjmVHwsgACtCMAAphLKUjeub7NKlvk2TgE")
    WELCOME_IMG_API   = os.environ.get("WELCOME_IMG_API", "https://api.aniwallpaper.workers.dev/random?type=girl")
    MASSAGE_IMG_URL   = os.environ.get("MASSAGE_IMG_URL", "https://i.ibb.co/pr2H8cwT/img-8312532076.jpg")

    # Aria2
    ARIA2C_HOST   = os.environ.get("ARIA2C_HOST", "http://localhost")
    ARIA2C_PORT   = int(os.environ.get("ARIA2C_PORT", 6800))
    ARIA2C_SECRET = os.environ.get("ARIA2C_SECRET", "")

    # Google Drive
    GDRIVE_FOLDER_ID = os.environ.get("GDRIVE_FOLDER_ID", "")
    TOKEN_PICKLE     = os.environ.get("TOKEN_PICKLE_PATH", "token.pickle")

    # RClone
    RCLONE_PATH      = os.environ.get("RCLONE_PATH", "rclone")
    RCLONE_CONFIG    = os.environ.get("RCLONE_CONFIG_PATH", "rclone.conf")

    # All admins combined
    @classmethod
    def is_admin(cls, user_id: int) -> bool:
        return user_id == cls.OWNER_ID or user_id in cls.SUDO_USERS
