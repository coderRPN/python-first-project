from popquiz.Question import Question

question_prompts = [
    "What color are apples?\n(a) Red/Green\n(b) Blue/purple\n(c)Yellow\n\n",
    "What color are bananas?\n(a) Red/Green\n(b) Blue/purple\n(c)Yellow\n\n",
    "what color are blueberries?\n(a) Red/Green\n(b) Blue/purple\n(c)Yellow\n\n"
]

questions = [
    Question(input(question_prompts[0]), "a"),
    Question(input(question_prompts[1]), "c"),
    Question(input(question_prompts[2]), "b"),
]


def run(questions):
    score = 0
    for question in questions:
        answer = question.prompt
        if answer == question.answer:
            score += 1
    print("\nYou've got " + str(score) + "/" + str(len(questions)) + " correct")


run(questions)
