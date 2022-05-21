import answers
import questions
import random
import os
import time

questions_count = len(questions.questions)
question_list = [x for x in range(1,questions_count+1)]
random.shuffle(question_list)
os.system('clear || cls')
quiz_length = ''

while True:
    try:
        quiz_length = int(input(
        f'How many questions would you like to include(max {questions_count})?'))
    except ValueError:
        print('Please enter a numerical value')
    if quiz_length > questions_count:
        print(f'Value to high, please select a number thats lower or equal to {questions_count}')
        quiz_length = ''
    else:
        break

current_question = 0
correct_answers = []
user_answers =[]
quiz_questions = []
while current_question <= quiz_length-1:
    # Get question
    question = questions.questions[question_list[current_question]]
    # Add question to list
    quiz_questions.append(question)
    # Select correct answer
    correct = random.choice(answers.answers[question_list[current_question]]['correct'])
    # Select a answer that seems possible
    possible = random.choice(answers.answers[question_list[current_question]]['possible'])
    # Create a local list of wrong answers
    wrong = answers.answers[question_list[current_question]]['wrong']
    # Randomize wrong answers
    random.shuffle(wrong)
    # Select 2 wrong answers, pop them so they cant be used again
    wrong1 = wrong.pop()
    wrong2 = wrong.pop()
    # Add correct answer to correct answer list
    correct_answers.append(correct)
    # Answer options list
    answer_list = [correct, possible, wrong1, wrong2]
    # Randomize answer option list
    random.shuffle(answer_list)

    while True:
        user_answer = ''
        try:
            os.system('clear || cls')
            print(f'Question {current_question+1}:{question}', end="\n"*2)
            for x in range(len(answer_list)):
                print(f'{x+1}. {answer_list[x]}')
            print('')
            user_answer = int(input('Select your answer: '))
        except ValueError:
            print('Please enter a number 1,2,3 or 4')
            time.sleep(2)
            continue
        if user_answer > 4:
            print('Please enter a number 1,2,3 or 4')
            time.sleep(2)
            continue
        if user_answer <= 4:
            user_answers.append(answer_list[user_answer-1])
            break
    current_question += 1

os.system('clear || cls')
print('Quiz Results')
correct_total = 0
for entry in range(len(correct_answers)):
    print(f'Question {entry+1}: {quiz_questions[entry]}')
    if correct_answers[entry] == user_answers[entry]:
        print(f'Correct! {user_answers[entry]}', end='\n'*4)
        correct_total += 1
    else:
        print(f'Your Answer: {user_answers[entry]}')
        print(f'Correct Answer: {correct_answers[entry]}', end='\n'*4)
score = 100*(correct_total/quiz_length)
print('', end='\n'*3)
print(f'Score: {round(score, 2)}')

while True:
    exit_phrase = input('Type exit to quit: ')
    if exit_phrase.lower() == 'exit':
        quit()