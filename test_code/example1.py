import os
import pickle

# Security issue: command injection
user_input = input("Enter command: ")
os.system(user_input)  # This is dangerous!

# Security issue: unsafe deserialization
data = pickle.loads(user_input)  # This is also dangerous!

print("Code execution complete")
