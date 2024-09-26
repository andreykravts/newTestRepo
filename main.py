import random


def get_simple_question():
    list_of_questions = []
    list_of_questions.append('Do you smart enough?')
    list_of_questions.append('How are you doing my friend?')
    list_of_questions.append('The weather is good today?')
    list_of_questions.append('Are you love hide and sick? ')
    list_of_questions.append('Where are you today?')
    list_of_questions.append('What is your favorite color?')
    return list_of_questions


def give_me_random_question(list_of_questions):
    # Generate a random integer between 1 and 5 (inclusive)
    random_number = random.randint(1, 5)
    print(list_of_questions[random_number])


def print_questions():
    list = get_simple_question()
    for i in range(1, 10):
        give_me_random_question(list)


if __name__ == '__main__':
    print_questions()
