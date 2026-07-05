# ========================================
# AI 증상 분석 프로그램
# Version 1.2 (Clean)
# Developer : 이서연
# ========================================

import datetime

print("=" * 40)
print("      AI 증상 분석 프로그램")
print("=" * 40)

print()
print("안녕하세요!")
print("이 프로그램은 입력한 증상을 분석하여")
print("가능성이 높은 질병을 예측해드립니다.")
print("*본 결과는 참고용이며 정확한 진단은 병원에서 받으세요.")

# -----------------------------
# 사용자 정보 입력
# -----------------------------

name = input("이름을 입력하세요 : ")

print()
print(f"반갑습니다, {name}님!")

age = int(input("나이를 입력하세요 : "))

print()
print(f"{age}세로 확인되었습니다.")

# -----------------------------
# 나이 분류
# -----------------------------

if age < 13:
    print("어린이입니다.")
elif age < 20:
    print("청소년입니다.")
elif age < 65:
    print("성인입니다.")
else:
    print("고령자이므로 빠른 진료를 권장합니다.")

# =============================
# 🔥 핵심: 증상 입력 (1번만)
# =============================

symptoms = [s.strip().lower() for s in input("증상을 입력하세요 : ").split(",") if s.strip()]

# -----------------------------
# 점수 시스템
# -----------------------------

scores = {
    "감기": 0,
    "독감": 0,
    "비염": 0,
    "소화기 질환": 0
}

# -----------------------------
# 증상 분석
# -----------------------------

for symptom in symptoms:

    if symptom == "기침":
        scores["감기"] += 2
        scores["독감"] += 2

    elif symptom == "열":
        scores["독감"] += 3
        scores["감기"] += 1

    elif symptom == "콧물":
        scores["비염"] += 3
        scores["감기"] += 1

    elif symptom == "복통":
        scores["소화기 질환"] += 3

# -----------------------------
# 결과 계산
# -----------------------------

result = max(scores, key=scores.get)
total = sum(scores.values())

print()
print("=" * 40)
print("AI 분석 결과")
print("=" * 40)

for disease, score in scores.items():
    if total == 0:
        percent = 0
    else:
        percent = (score / total) * 100

    print(f"{disease} 가능성 : {percent:.1f}%")

print("-" * 40)
print(f"최종 판단 : {result}")

# -----------------------------
# 결과 상세 출력 (시간 포함)
# -----------------------------

now = datetime.datetime.now()

print()
print("=" * 40)
print("AI 증상 분석 결과 (상세)")
print("=" * 40)

print(f"📅 분석 날짜 : {now.strftime('%Y-%m-%d')}")
print(f"🕒 분석 시간 : {now.strftime('%H:%M:%S')}")

print(f"환자 이름 : {name}")
print(f"나이 : {age}세")
print(f"입력 증상 : {', '.join(symptoms)}")

print("-" * 40)

if result == "감기":
    print("예상 질환 : 감기")
    print("주의사항 : 충분한 휴식을 취하세요.")
    print("추천 진료과 : 내과")
    print("응급도 : 🟢 낮음")

elif result == "독감":
    print("예상 질환 : 독감")
    print("주의사항 : 체온을 자주 확인하세요.")
    print("추천 진료과 : 내과")
    print("응급도 : 🟡 보통")

elif result == "비염":
    print("예상 질환 : 비염")
    print("주의사항 : 따뜻한 환경 유지")
    print("추천 진료과 : 이비인후과")
    print("응급도 : 🟢 낮음")

elif result == "소화기 질환":
    print("예상 질환 : 소화기 질환")
    print("주의사항 : 자극적인 음식 피하기")
    print("추천 진료과 : 소화기내과")
    print("응급도 : 🟡 보통")

print()
print("※ 본 결과는 참고용이며 정확한 진단은 의료기관에서 받으시기 바랍니다.")

# -----------------------------
# 다시 실행 여부
# -----------------------------

while True:

    answer = input("다시 분석하시겠습니까? (y/n) : ")

    if answer == "y":
        print("\n" + "=" * 40)
        print("재시작합니다...\n")
        break

    elif answer == "n":
        print("프로그램을 종료합니다.")
        exit()

    else:
        print("y 또는 n만 입력해주세요.")
