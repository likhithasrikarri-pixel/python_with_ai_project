import pandas as pd
import numpy as np
from functions import calculate_total, calculate_average, assign_grade, check_pass_fail

print("="*70)
print("   STUDENT PERFORMANCE ANALYTICS SYSTEM - FINAL PROJECT")
print("   Python with AI | EWB Assessment")
print("="*70)

df = pd.read_csv('students.csv')
df.columns = df.columns.str.strip()

print(f"\n[Q1] Total Students: {len(df)}")
print(f"Columns in your CSV: {list(df.columns)}")

# iloc vadutunam - column peru tho pani ledu - 100% safe
# 0=ID, 1=Name, 2=Dept, 3,4,5,6,7=5 Subjects, 8=Attendance
totals, avgs, grades, results = [], [], [], []

for i in range(len(df)):
    marks = df.iloc[i, 3:8].tolist()  # 5 subjects marks
    att = df.iloc[i, 8]  # attendance
    totals.append(calculate_total(marks))
    avgs.append(calculate_average(marks))
    grades.append(assign_grade(calculate_average(marks)))
    results.append(check_pass_fail(calculate_average(marks), att))

df['Total'] = totals
df['Average'] = np.round(avgs, 2)
df['Grade'] = grades
df['Result'] = results

print("\n[Q2] Results Table:")
print(df.to_string(index=False))

print("\n" + "="*70)
print("ANSWERS FOR ALL QUESTIONS")
print("="*70)

print(f"\n[Q3] Class Average: {df['Average'].mean():.2f}")
print(f"[Q4] Highest: {df['Average'].max()} - {df.iloc[df['Average'].idxmax(), 1]}")
print(f"[Q5] Lowest: {df['Average'].min()} - {df.iloc[df['Average'].idxmin(), 1]}")
print(f"\n[Q6] Pass: {len(df[df['Result']=='Pass'])} | [Q7] Fail: {len(df[df['Result']=='Fail'])}")
print(f"[Q8] Fail List: {', '.join(df[df['Result']=='Fail'].iloc[:,1].tolist()) if len(df[df['Result']=='Fail'])>0 else 'None'}")

print("\n[Q9] Grade Count:")
print(df['Grade'].value_counts().to_string())

print("\n[Q10] Subject-wise Stats:")
for j in range(3, 8):
    col = df.iloc[:, j]
    print(f"  {df.columns[j]}: Highest={int(col.max())}, Lowest={int(col.min())}, Avg={float(col.mean()):.2f}")

print("\n[Q11] Dept-wise Average:")
print(df.groupby(df.columns[2])['Average'].mean().round(2).to_string())

print("\n[Q12] Top 5 Performers:")
top5 = df.sort_values(by='Average', ascending=False).head(5)
for k, (idx, r) in enumerate(top5.iterrows(), 1):
    print(f"  {k}. {r.iloc[1]} - {r['Average']} - {r['Grade']}")

print("\n[Q13] Attendance <70:")
low = df[df.iloc[:,8] < 70]
print(low.iloc[:, [1,8]].to_string(index=False) if len(low)>0 else "  None")

print(f"\n[Q14] Sum of all Total Marks: {int(np.sum(df['Total']))}")
print(f"[Q15] Best in {df.columns[3]}: {df.iloc[df.iloc[:,3].idxmax(),1]} - {df.iloc[:,3].max()}")

print("\n" + "="*70)
print("--- Project Successfully Completed ---")
print("="*70)