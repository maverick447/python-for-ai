from dotenv import load_dotenv
import os

# Load the .env file
load_dotenv() # middle is the path to .env 
#load_dotenv(dotenv_path='code/.env')

#load_dotenv(dotenv_path='environment/.env')

# Now use your variables
api_key = os.environ.get('API_KEY')
database_key = os.environ.get('DATABASE_URL')
debug = os.environ.get('DEBUG')

print(f"API Key: {api_key}")
print(f"Debug mode: {debug}")
print(f"Database key: {database_key}")