import numpy as np
from pathlib import Path
from faker import Faker
from openpyxl import Workbook

np.random.seed(7)
N = 10
faker = Faker("ko_KR")
# print(faker.name())
# print(faker.email())
# print(faker.job())
names = [faker.name() for _ in range(N)]
emails = [faker.email() for _ in range(N)]
scores = np.random.randint(50, 101, size=(N, 3))  # 50~100점 사이의 정수 난수 생성  
#print(scores)
total_scores = scores.sum(axis=1) # 각 학생의 총점 계산
avg_scores = scores.mean(axis=1)  # 각 학생의 평균 계산
#print(total_scores)
#print(avg_scores)
wb = Workbook()
ws = wb.active
ws.title = "학생성적"
headers = ["이름", "이메일", "국어", "영어", "수학", "총점", "평균"]
ws.append(headers)
for idx in range(N):
    row = [
        names[idx],
        emails[idx],
        scores[idx, 0],
        scores[idx, 1],
        scores[idx, 2],
        total_scores[idx],
        round(avg_scores[idx], 2)
    ]
    ws.append(row)  
file_path = Path(__file__).parent / "student_scores.xlsx"    
wb.save(file_path)