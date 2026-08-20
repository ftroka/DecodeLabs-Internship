def run_quiz():
    questions = [
        {
            "question": "What is the capital of France?",
            "answer": "paris"
        },
        {
            "question": "Which planet is known as the Red Planet?",
            "answer": "mars"
        },
        {
            "question": "What is the largest ocean on Earth?",
            "answer": "pacific"
        },
        {
            "question": "Who wrote Romeo and Juliet?",
            "answer": "shakespeare"
        },
        {
            "question": "What is the chemical symbol for water?",
            "answer": "h2o"
        }
    ]

    score = 0

    print("=" * 50)
    print("GENERAL KNOWLEDGE QUIZ")
    print("=" * 50)

    for index, item in enumerate(questions, start=1):
        print(f"\nQuestion {index}:")
        print(item["question"])

        user_answer = input("Your answer: ")

        normalized_answer = user_answer.strip().lower()

        if normalized_answer == item["answer"]:
            print(" Correct!")
            score += 1
        else:
            print(f" Wrong! Correct answer: {item['answer'].title()}")

    print("\n" + "=" * 50)
    print("QUIZ COMPLETED")
    print("=" * 50)

    print(f"Final Score: {score}/{len(questions)}")

    percentage = (score / len(questions)) * 100
    print(f"Percentage: {percentage:.2f}%")

    if percentage >= 80:
        print("Excellent!")
    elif percentage >= 50:
        print("Good Job!")
    else:
        print("Keep Practicing!")

run_quiz()