import os
from dotenv import load_dotenv

load_dotenv()

BOT_TOKEN = os.getenv("BOT_TOKEN")
ADMIN_CHAT_ID = str(os.getenv("ADMIN_CHAT_ID", "714948319"))  # Convert to string
BACKEND_URL = "https://gulqand.onrender.com/api/orders/"  # Updated URL for Render
MEDIA_URL = "https://gulqand.onrender.com"

# Notification settings (default: enabled)
NOTIFICATIONS_ENABLED = True
NOTIFICATION_SOUND = True