import os

def run_command(cmd):
    os.system(cmd)  # 명백한 보안 취약점 (Command Injection)

run_command("rm -rf /")  
