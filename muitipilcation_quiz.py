import pyinputplus as pyip
import random
import time

number_of_questions = 10
correct_answers = 0


# for question_number in range(number_of_questions):
#     # Pick two random numbers between 1 and 9
#     num1 = random.randint(1, 9)
#     num2 = random.randint(1, 9)
#     prompt = f'#{question_number}: {num1} x {num2} = '
#     try:
#         pyip.inputStr(prompt, allowRegexes=[f'^{num1*num2}$'], blockRegexes=[('.*', 'Incorrect!')], timeout=8, limit=3)
#     except pyip.TimeoutException:
#         print('Out of time!')
#     except pyip.RetryLimitException:
#         print('Out of tries!')
#     else:
#         print('Correct!')
#         correct_answers += 1
#     time.sleep(1)
#     print(f'Score: {correct_answers}/{number_of_questions}')


# the traditional way
for question_number in range(number_of_questions):
    num1 = random.randint(1, 9)
    num2 = random.randint(1, 9)
    prompt = f'#{question_number}: {num1} x {num2} = '
    max_wrong_attempts = 3
    wrong_attempts = 0
    start_time = 0
    end_time = 0
    while True:
        try:
            start_time = time.time()
            answer = input(prompt)
            end_time = time.time()
            if end_time - start_time >= 8:
                raise Exception('Out of time!')
            if int(answer) == num1 * num2:
                print('Correct!')
                correct_answers += 1
            else:
                wrong_attempts += 1
                raise Exception('Incorrect!')
        except Exception:
            if end_time - start_time >= 8:
                print('Out of time!')
                break
            if wrong_attempts >= max_wrong_attempts:
                print('Out of tries!')
                break
        else:
            break
    print(f'Score: {correct_answers}/{number_of_questions}')