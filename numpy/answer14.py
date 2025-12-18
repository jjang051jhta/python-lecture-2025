import numpy as np
from pathlib import Path
from faker import Faker
from openpyxl import Workbook, load_workbook

"""
np.random.seed(7)
N = 10
faker = Faker("ko_KR")
faker.seed_instance(7)
# print(faker.name())
# print(faker.email())
# print(faker.job())
names = [faker.name() for _ in range(N)]
emails = [faker.email() for _ in range(N)]
scores = np.random.randint(50, 101, size=(N, 3))  # 50~100점 사이의 정수 난수 생성  
print(names)

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
"""
current_dir = Path(__file__).resolve().parent
wb = load_workbook(current_dir / "student_scores.xlsx")
ws =  wb.active
rows = []

for row in ws.iter_rows(min_row=2, max_row=ws.max_row, values_only=True):
    rows.append(list(row))

# for row in range(2, ws.max_row + 1):
#     rows.append([
#             ws[f"A{row}"].value,
#             ws[f"B{row}"].value,  
#             ws[f"C{row}"].value,
#             ws[f"D{row}"].value,
#             ws[f"E{row}"].value,
#             ws[f"F{row}"].value,
#             ws[f"G{row}"].value
#     ])
#print(rows)    
data = np.array(rows, dtype=object)  # object로 해야 숫자도 같이 들어감
print(data)
avg_scores = data[:, 6].astype(int)  # 국어, 영어, 수학 점수 부분만 추출하여 정수형으로 변환
print(avg_scores)
mask =  avg_scores >= 70
passed_students = data[mask]
print(passed_students)
wb = Workbook()
ws = wb.active
ws.title = "성적70점이상"
headers = ["이름", "이메일", "국어", "영어", "수학", "총점", "평균"]
ws.append(headers)
for row in passed_students:
    ws.append(row.tolist())
file_path = Path(__file__).parent / "student_passed.xlsx"    
wb.save(file_path)
    