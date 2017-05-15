########################################################################################################################
#   William Crabtree                                                                                                   #
#   30Mar17                                                                                                            #
#   Purpose: Compare students answers to an answer file, the inform user if they passed or failed.                     #
########################################################################################################################

#   Open answer file and student asnwers file

answerFile = open("answers.txt", "r").readlines()
try:
    studentAnswer = open(input("Please give the direct path to the student answer file. "), "r").readlines()
except OSError:
    print("That path doesn't look right.")
    exit()

#   Compare answer file to student answers

score = 0
questionNumber = 0
incorrectAnswers = []

#   If question is right, score and question umber go up
#   If wrong, question number goes up and incorrect answer is saved to list

while questionNumber < len(answerFile):
    if answerFile[questionNumber] == studentAnswer[questionNumber]:
        score += 1
        questionNumber += 1
    else:
        questionNumber += 1
        incorrectAnswers.append(questionNumber)

#   Compare the total score

if score >= 15:
    print("You passed with", score, "total right answers and", 20 - score, "wrong.")
    print("The incorrect answers are: ", incorrectAnswers)
else:
    print("You failed with", score, "total right answers and", 20 - score, "wrong.")
    print("The incorrect answers are:", incorrectAnswers)
