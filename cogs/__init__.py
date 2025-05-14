# Credits: R.O.D
# This file ensures the 'cogs' directory is treated as a valid Python package.

# Import all cogs automatically when the package is loaded
# This allows dynamic loading of cogs from the cogs directory

import os
import importlib

def setup(bot):
    # Loop through all files in the current directory
    for filename in os.listdir(os.path.dirname(__file__)):
        # Check for Python files that are not __init__.py
        if filename.endswith(".py") and filename != "__init__.py":
            # Import the cog dynamically
            cog_name = f"cogs.{filename[:-3]}"
            cog_module = importlib.import_module(cog_name)
            if hasattr(cog_module, "setup"):
                cog_module.setup(bot)
