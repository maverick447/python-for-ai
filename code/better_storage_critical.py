import os

# Mac/Linux - bad/cumbersome way to enter the environment 
#export API_KEY=sk-1234567890abcdef
#python correct_storage_critical.py 
'''
(.venv) ramapra_mini@mini python-for-ai % export API_KEY=sk-1234567890abcdef
(.venv) ramapra_mini@mini python-for-ai % python3 code/correct_storage_critical.py
sk-1234567890abcdef
(.venv) ramapra_mini@mini python-for-ai % 
'''

# Method 1: Get with default
api_key = os.environ.get('API_KEY', 'demo-key')

# Method 2: Check if exists
if 'API_KEY' in os.environ:
    api_key = os.environ['API_KEY']
else:
    print("No API key found")

# Method 3: Will crash if not found
try:
    api_key = os.environ['API_KEY']  # KeyError if missing!
    print(api_key)
except KeyError:
    print("API_KEY environment variable not set!")
    #api_key = 'demo-key'  # Fallback to demo key    
