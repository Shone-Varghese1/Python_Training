# 8. Quiz File Generator
#
# Write a function that takes a list of questions and writes them into quiz.txt with question numbers.
# Include blank lines for answers.



questions = {
    1: "Capital of Kerala:",
    2: "Capital of Tamil Nadu:",
    3: "Capital of Karnataka:",
    4: "Capital of Andhra Pradesh:",
    5: "Capital of Telangana:",
    6: "Capital of Maharashtra:",
    7: "Capital of Gujarat:",
    8: "Capital of Rajasthan:",
    9: "Capital of Uttar Pradesh:",
    10: "Capital of Bihar:"
}


def gen_quiz_file(question,i):
    with open("./textfiles/quiz_file.txt", "a") as f:
        f.write(f"{i}: {question}\n\n\n")
i=1
for q in questions.values():
    gen_quiz_file(q,i)
    i+=1


