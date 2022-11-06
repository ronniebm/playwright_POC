from dotenv import load_dotenv
import os

# You need to have a .env file in your local root directory,
# this will be loaded automatically when calling load_dotenv().
load_dotenv()

# Environment settings.
ENV_URL = os.getenv('ENV_URL')

# User credential settings.
ANALYST_CREDENTIALS = (os.getenv('ANALYST_NAME'), os.getenv('ANALYST_PASS'))
MANAGER_CREDENTIALS = (os.getenv('MANAGER_NAME'), os.getenv('MANAGER_PASS'))

# Client and Service settings.
CLIENT_AND_SERVICE = (os.getenv('CLIENT_NAME'), os.getenv('SERVICE_NAME'))
