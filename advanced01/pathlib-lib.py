import os
from pathlib import Path

print(f"os.getcwd() : {os.getcwd()}")
print(f"Path.cwd() : {Path.cwd()}")

os.makedirs("a/b/c", exist_ok=True)
Path("d/e/f").mkdir(parents=True, exist_ok=True)

print(os.path.exists("hello.txt"))
print(Path("hello.txt").exists())

print(os.path.isfile("hello.txt"))
print(Path("hello.txt").is_file())

# os.remove("hello.txt")
Path("hello.txt").unlink()  # 제거

# Path는 경로 또는 파일 찾을때 사용
# os low-level 명령어들 쓸때 사용
