name = input("Enter the test name: ")
score = int(input("Enter the score you recieved: "))
max_score = int(input("Enter the maximum score: "))

letter_grade = ""

percentage = round((score / max_score) * 100, 2)

if percentage >= 90:
  letter_grade = "A+"
elif percentage >= 80:
  letter_grade = "A"
elif percentage >= 70:
  letter_grade = "B"
elif percentage >= 60:
  letter_grade = "C"
elif percentage >= 50:
  letter_grade = "D"
else:
  letter_grade = "U"

print(f"Test Name: {name} \nScore: {score}/{max_score} \nGrade: {letter_grade} \nPercentage: {percentage}"
)
