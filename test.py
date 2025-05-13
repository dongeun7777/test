import os
import subprocess
import pickle

def run_command(user_input):
    os.system(user_input)  # 취약점: Command Injection

DB_PASSWORD = "supersecretpassword"  # 취약점: Hardcoded Password

def load_data(serialized_data):
    return pickle.loads(serialized_data)  # 취약점: Insecure Deserialization

def run_subprocess(user_input):
    subprocess.call(user_input, shell=True)  # 취약점: shell=True 사용

def find_user(username):
    query = f"SELECT * FROM users WHERE name = '{username}'"  # 취약점: SQL Injection
    print("Running Query:", query)

if __name__ == "__main__":
    user_input = "echo Vulnerable!"
    run_command(user_input)
    run_subprocess(user_input)
    serialized = pickle.dumps({"key": "value"})
    load_data(serialized)
    find_user("admin' OR '1'='1")
