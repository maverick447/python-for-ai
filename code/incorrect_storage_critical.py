# BAD: Never hardcode sensitive data!
api_key = "sk-1234567890abcdef"  # Everyone can see this!
database = "production_database"  # Can't change without editing code

# bad method of adding sensitive info
print(f"{api_key=}, {database=}")
