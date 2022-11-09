from dotenv import load_dotenv
import os

# You need to have a .env file in your local root directory,
# this will be loaded automatically when calling load_dotenv().
load_dotenv()

# Environment settings.
ENV = os.getenv('ENV')
ENV_URL = os.getenv(f'{ENV}_ENV_URL')
CLIENT = os.getenv('CLIENT')

# User credential settings.
ANALYST_CREDENTIALS = (os.getenv(f'{ENV}_ANALYST_NAME'), os.getenv(f'{ENV}_ANALYST_PASS'))
MANAGER_CREDENTIALS = (os.getenv(f'{ENV}_MANAGER_NAME'), os.getenv(f'{ENV}_MANAGER_PASS'))
VIEWPORT = {'width': int(os.getenv('WIDTH')), 'height': int(os.getenv('HEIGHT'))}

# Client and Service settings.
CLIENT_AND_SERVICE = (os.getenv(f'CLIENT_{CLIENT}'), os.getenv('SERVICE'))
