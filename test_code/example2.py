import subprocess
import eval

# Security issue: unsafe subprocess
subprocess.call(["rm", "-rf", "/"])  # Very dangerous!

# Security issue: using eval
result = eval("2 + 2")  # Should use ast.literal_eval
print(f"Result: {result}")

# Hardcoded password (security issue)
password = "mysecretpassword123"
