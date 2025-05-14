# Credits: R.O.D
# Configuration file for the Discord Moderation Bot

# Bot Token
# Replace this with your bot's token from the Discord Developer Portal
BOT_TOKEN = "YOUR_BOT_TOKEN_HERE"

# Command Prefix
# This defines the prefix for bot commands (e.g., !kick, !ban)
COMMAND_PREFIX = "!"

# Default Role Configuration
# Role names can be configured here for muting, admin, etc.
DEFAULT_MUTED_ROLE = "Muted"  # Name of the role used for muting members

# Permissions
# Set permissions for commands if needed
REQUIRED_PERMISSIONS = {
    "kick": "Kick Members",
    "ban": "Ban Members",
    "mute": "Manage Roles",
    "unmute": "Manage Roles",
}

# Welcome Messages
# Set this to True if you want the bot to send a welcome message when a new member joins
WELCOME_MESSAGES_ENABLED = True

# Custom Welcome Messages (Optional)
CUSTOM_WELCOME_MESSAGE = "Welcome to the server, {member}! Be sure to check the rules and have fun!"

# Logging Configuration
# Enable or disable logging of bot actions
LOGGING_ENABLED = True
LOG_FILE_NAME = "bot_activity.log"

# Debug Mode
# Set this to True for debugging purposes (e.g., detailed error messages)
DEBUG_MODE = False
