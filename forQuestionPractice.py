from QuestionFile import QuestionClass

question_prompts = [
    "What is the last name of Jim in the TV show The Office?\n(a) Halpert\n(b) Schrute\n(c) Weasley\n(d) Scott\n\n",
    "What is the last movie Sean Connery appeared in as James Bond?\n(a) Dr. No\n(b) Skyfall\n(c) Thunderball\n(d) Diamonds are Forever\n\n",
    "What is the name of the author of James Bond novels?\n(a) Jean Le Carre\n(b) Robert Ludlum\n(c) Ian Fleming\n(d) Lee Childs\n\n"
]

questions_answers = [
    QuestionClass(question_prompts[0], "a"),
    QuestionClass(question_prompts[1], "d"),
    QuestionClass(question_prompts[2], "c")
]

def run_test(questions_answers):
    score = 0
    for question in questions_answers:
        answer = input(question.prompt)
        if answer == question.answer:
            score += 1
    print("You got " + str(score) + " out of " + str(len(questions_answers)) + " right.")


run_test(questions_answers)
