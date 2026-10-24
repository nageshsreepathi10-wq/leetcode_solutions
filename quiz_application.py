
questions = [
    {
        "question": "1. Which keyword is used to define a function in Python?",
        "options": ["A. func", "B. def", "C. function", "D. define"],
        "answer": "B"
    },
    {
        "question": "2. Which data type stores True or False?",
        "options": ["A. int", "B. str", "C. bool", "D. list"],
        "answer": "C"
    },
    {
        "question": "3. Which symbol is used for comments in Python?",
        "options": ["A. //", "B. <!-- -->", "C. **", "D. #"],
        "answer": "D"
    },
    {
        "question": "4. Which data structure stores multiple items in order?",
        "options": ["A. list", "B. int", "C. float", "D. bool"],
        "answer": "A"
    },
    {
        "question": "5. What is the output of print(2 + 3)?",
        "options": ["A. 23", "B. 6", "C. 5", "D. 2 + 3"],
        "answer": "C"
    }
]

score = 0

print("===== PYTHON QUIZ APPLICATION =====")
print("Choose your answer: A, B, C, or D\n")

for item in questions:
    print(item["question"])

    for option in item["options"]:
        print(option)

    user_answer = input("Your answer: ").strip().upper()

    if user_answer not in ["A", "B", "C", "D"]:
        print("Invalid option! No point awarded.")
    elif user_answer == item["answer"]:
        print("Correct answer!")
        score += 1
    else:
        print("Wrong answer!")
        print("Correct answer:", item["answer"])

    print()

print("===== QUIZ RESULTS =====")
print("Total questions:", len(questions))
print("Correct answers:", score)
print("Wrong answers:", len(questions) - score)
print("Final score:", str(score) + "/" + str(len(questions)))
print("Percentage:", str(round(score / len(questions) * 100, 2)) + "%")
