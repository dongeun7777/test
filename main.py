import os
import subprocess
import pickle

# 1. Command Injection (명령어 주입)
def run_command(user_input):
    os.system(user_input)  # 취약점: 사용자 입력을 그대로 명령어로 실행

# 2. Hardcoded Password (하드코딩된 비밀번호)
DB_PASSWORD = "supersecretpassword"  # 취약점: 비밀번호 하드코딩

# 3. Insecure Deserialization (비검증 역직렬화)
def load_data(serialized_data):
    return pickle.loads(serialized_data)  # 취약점: 안전하지 않은 데이터 역직렬화

# 4. Subprocess with Shell=True (명령어 인젝션 위험)
def run_subprocess(user_input):
    subprocess.call(user_input, shell=True)  # 취약점: shell=True 사용

# 5. SQL Injection (SQL 인젝션, 예시용)
def find_user(username):
    query = f"SELECT * FROM users WHERE name = '{username}'"  # 취약점: 사용자 입력 직접 포함
    print("Running Query:", query)  # 실제 DB 연결은 생략

# 테스트 실행 (일부러 취약 코드 호출)
if __name__ == "__main__":
    user_input = "echo Vulnerable!"
    run_command(user_input)
    run_subprocess(user_input)
    serialized = pickle.dumps({"key": "value"})
    load_data(serialized)
    find_user("admin' OR '1'='1")
